import heapq

# Graph Romania (disederhanakan contoh klasik AI)
romania_map = {
    'Arad': {'Zerind': 75, 'Sibiu': 140, 'Timisoara': 118},
    'Zerind': {'Arad': 75, 'Oradea': 71},
    'Oradea': {'Zerind': 71, 'Sibiu': 151},
    'Timisoara': {'Arad': 118, 'Lugoj': 111},
    'Lugoj': {'Timisoara': 111, 'Mehadia': 70},
    'Mehadia': {'Lugoj': 70, 'Drobeta': 75},
    'Drobeta': {'Mehadia': 75, 'Craiova': 120},
    'Craiova': {'Drobeta': 120, 'Rimnicu Vilcea': 146, 'Pitesti': 138},
    'Sibiu': {'Arad': 140, 'Oradea': 151, 'Fagaras': 99, 'Rimnicu Vilcea': 80},
    'Rimnicu Vilcea': {'Sibiu': 80, 'Craiova': 146, 'Pitesti': 97},
    'Fagaras': {'Sibiu': 99, 'Bucharest': 211},
    'Pitesti': {'Rimnicu Vilcea': 97, 'Craiova': 138, 'Bucharest': 101},
    'Bucharest': {'Fagaras': 211, 'Pitesti': 101, 'Giurgiu': 90},
    'Giurgiu': {'Bucharest': 90}
}

# Heuristic (straight-line distance to Bucharest)
heuristic = {
    'Arad': 366, 'Bucharest': 0, 'Craiova': 160, 'Drobeta': 242,
    'Fagaras': 176, 'Giurgiu': 77, 'Lugoj': 244, 'Mehadia': 241,
    'Oradea': 380, 'Pitesti': 100, 'Rimnicu Vilcea': 193,
    'Sibiu': 253, 'Timisoara': 329, 'Zerind': 374
}

# ---------- BFS ----------
def bfs(start, goal):
    queue = [[start]]
    visited = set()
    while queue:
        path = queue.pop(0)
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            for neighbor in romania_map.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None

# ---------- DFS ----------
def dfs(start, goal):
    stack = [[start]]
    visited = set()
    while stack:
        path = stack.pop()
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            for neighbor in romania_map.get(node, []):
                new_path = list(path)
                new_path.append(neighbor)
                stack.append(new_path)
            visited.add(node)
    return None

# ---------- UCS ----------
def ucs(start, goal):
    queue = [(0, [start])]
    visited = set()
    while queue:
        cost, path = heapq.heappop(queue)
        node = path[-1]
        if node == goal:
            return path, cost
        if node not in visited:
            for neighbor, weight in romania_map.get(node, {}).items():
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(queue, (cost + weight, new_path))
            visited.add(node)
    return None

# ---------- Greedy Best First Search ----------
def gbfs(start, goal):
    queue = [(heuristic[start], [start])]
    visited = set()
    while queue:
        _, path = heapq.heappop(queue)
        node = path[-1]
        if node == goal:
            return path
        if node not in visited:
            for neighbor in romania_map.get(node, {}):
                new_path = list(path)
                new_path.append(neighbor)
                heapq.heappush(queue, (heuristic[neighbor], new_path))
            visited.add(node)
    return None

# ---------- A* ----------
def astar(start, goal):
    queue = [(heuristic[start], 0, [start])]
    visited = set()
    while queue:
        est_total, cost, path = heapq.heappop(queue)
        node = path[-1]
        if node == goal:
            return path, cost
        if node not in visited:
            for neighbor, weight in romania_map.get(node, {}).items():
                new_path = list(path)
                new_path.append(neighbor)
                g = cost + weight
                f = g + heuristic[neighbor]
                heapq.heappush(queue, (f, g, new_path))
            visited.add(node)
    return None

# ---------- Main ----------
if __name__ == "__main__":
    print("Pilihan Algoritma: BFS | DFS | UCS | GBFS | A*")
    algo = input("Masukkan algoritma: ").upper()
    start = input("Kota awal: ")
    goal = input("Kota tujuan: ")

    if algo == "BFS":
        print("Path:", bfs(start, goal))
    elif algo == "DFS":
        print("Path:", dfs(start, goal))
    elif algo == "UCS":
        path, cost = ucs(start, goal)
        print("Path:", path, "Cost:", cost)
    elif algo == "GBFS":
        print("Path:", gbfs(start, goal))
    elif algo == "A*":
        path, cost = astar(start, goal)
        print("Path:", path, "Cost:", cost)
    else:
        print("Algoritma tidak dikenali.")