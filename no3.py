import heapq

# Inisialisasi dictionary kosong untuk mepresentasikan graf jaringan jalan di Romania.
jalur = {}

# Definisi kelas PriorityQueue untuk implementasi antrian prioritas.
class PriorityQueue:
    def __init__(self) -> None:
        self.cities = [] # inisialisasi daftar kosong utnuk menyimpan elemen antrian prioritas.
        
    def isEmpty(self):
        if self.cities == []:
            return True
        return False
    
    def check(self):
        print(self.cities)

    def push(self, city, cost):
        heapq.heappush(self.cities, (cost, city)) # Menambahkan elemen ke antrian prioritas berdasarkan biaya.

    def pop(self):
        return heapq.heappop(self.cities)[1] # Menghapus dan mengembalikan elemen dengan biaya terendah
    
# Definisi kelas CityNode untuk merepresentasikan node kota dalam graf.
class CityNode:
    def __init__(self, city, distance) -> None:
        self.city = str(city)
        self.distance = str(distance)

def MakeDict():
    file_jalan = "greedy/jalan.txt" # Ganti sesuai path masing masing"
    file = open(file_jalan, 'r')
    for str in file:
        delimeter = str.split(',')
        city1 = delimeter[0]
        city2 = delimeter[1]
        dist = delimeter[2]

        jalur.setdefault(city1, []).append(CityNode(city2, dist))

# Fungsi untuk membaca file teks yang berisi nilai heuristik dan membangun dictyionary nilai heuristik "h"
def makeHeuristicDict():
    h = {}
    file_heuristic_jalan = "greedy/heuristic_jalan.txt" #ganti path sesuai device
    file = open(file_heuristic_jalan, 'r')
    for str in file:
        delimeter = str.strip().split(',')
        node = delimeter[0].strip()
        sld = int(delimeter[1].strip()) # Jalan lurus
        h[node] = sld

    return h

# Fungsi heuristik yang digunakan dalam pencarian GBFS.
def heuristic(node, values):
    return values[node]

# Fungsi utama yang menjalankan algoritma GBFS.
def greedyBFS(start, end):
    path = {}
    q = PriorityQueue()
    h = makeHeuristicDict()

    q.push(start, 0)
    path[start] = None
    expeand_list = []

    while q.isEmpty() == False:
        curr = q.pop()
        expeand_list.append(curr)

        if curr == end:
            break

        for new in jalur[curr]:
            if new.city not in path:
                f_cost = heuristic(new.city, h)
                q.push(new.city, f_cost)
                path[new.city] = curr

    # Fungsi untuk mencetak output hasil pencarian.
    printOutput(start, end, path, expeand_list)

def printOutput(start, end, path, expandlist):
    finalpath = []
    i = end

    while(path.get(i) != None):
        finalpath.append(i)
        i = path[i]
    finalpath.append(start)
    finalpath.reverse()

    print("Program Greedy Best-First Search")
    print(start + " => " + end)
    print("Kota yang dilewati dengan jarak terpendek\t: " + str(finalpath))

# Fungsi utama yang dijalankan saat skrip ini dieksekusi.

def main():
    src = "Arad"
    dst = "Bucharest"
    MakeDict()
    greedyBFS(src, dst)

# Pengecekan apakah skrip ini dijalankan sebagai program utama.
if __name__ == "__main__":
    main()