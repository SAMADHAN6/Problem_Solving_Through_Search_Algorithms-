import heapq
import time

# DIFFERENT GRAPH FOR BFS, DFS AND A*

graph = {
    'S': {'A': 1, 'B': 1},
    'A': {'G': 10},
    'B': {'C': 1},
    'C': {'G': 1},
    'G': {}
}

# Heuristic values for A*
heuristic = {
    'S': 3,
    'A': 10,
    'B': 2,
    'C': 1,
    'G': 0
}


# BFS

def bfs(graph, start, goal):
    queue = [[start]]
    visited = set()
    nodes = 0

    while queue:
        path = queue.pop(0)
        node = path[-1]

        nodes += 1

        if node == goal:
            return path, nodes

        if node not in visited:
            visited.add(node)

            for neighbour in graph[node]:
                new_path = list(path)
                new_path.append(neighbour)
                queue.append(new_path)

    return None, nodes


# DFS

def dfs(graph, start, goal):
    stack = [[start]]
    visited = set()
    nodes = 0

    while stack:
        path = stack.pop()
        node = path[-1]

        nodes += 1

        if node == goal:
            return path, nodes

        if node not in visited:
            visited.add(node)

            for neighbour in reversed(list(graph[node])):
                new_path = list(path)
                new_path.append(neighbour)
                stack.append(new_path)

    return None, nodes


# A STAR

def astar(graph, start, goal, h):
    pq = []

    # (f, node, path, g)
    heapq.heappush(pq, (h[start], start, [start], 0))

    visited = set()
    nodes = 0

    while pq:
        f, node, path, cost = heapq.heappop(pq)

        nodes += 1

        if node == goal:
            return path, nodes, cost

        if node not in visited:
            visited.add(node)

            for neighbour, weight in graph[node].items():
                g = cost + weight
                f = g + h[neighbour]

                heapq.heappush(
                    pq,
                    (f, neighbour, path + [neighbour], g)
                )

    return None, nodes, None


# RUN BFS

start = time.time()
bfs_path, bfs_nodes = bfs(graph, 'S', 'G')
bfs_time = time.time() - start

print("----- BFS -----")
print("Path:", " -> ".join(bfs_path))
print("Nodes explored:", bfs_nodes)
print("Execution time:", bfs_time, "seconds")


# RUN DFS

start = time.time()
dfs_path, dfs_nodes = dfs(graph, 'S', 'G')
dfs_time = time.time() - start

print("\n----- DFS -----")
print("Path:", " -> ".join(dfs_path))
print("Nodes explored:", dfs_nodes)
print("Execution time:", dfs_time, "seconds")


# RUN A*

start = time.time()
astar_path, astar_nodes, astar_cost = astar(
    graph, 'S', 'G', heuristic
)
astar_time = time.time() - start

print("\n----- A* -----")
print("Path:", " -> ".join(astar_path))
print("Nodes explored:", astar_nodes)
print("Path cost:", astar_cost)
print("Execution time:", astar_time, "seconds")
