from collections import deque

graph = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D', 'E'],
    'D': ['B', 'C', 'E', 'F'],
    'E': ['C', 'D', 'F'],
    'F': ['D', 'E']
}

# DFS
def dfs(graph, start, goal, path=None):
    if path is None:
        path = []
    path = path + [start]
    if start == goal:
        return path
    for neighbor in graph[start]:
        if neighbor not in path:
            new_path = dfs(graph, neighbor, goal, path)
            if new_path:
                return new_path
    return None

# BFS
def bfs(graph, start, goal):
    queue = deque([[start]])
    visited = set()
    while queue:
        path = queue.popleft()
        node = path[-1]
        if node == goal:
            return path
        elif node not in visited:
            for neighbor in graph[node]:
                new_path = list(path)
                new_path.append(neighbor)
                queue.append(new_path)
            visited.add(node)
    return None

start, goal = 'A', 'F'
print("Шлях DFS від A до F:", dfs(graph, start, goal))
print("Шлях BFS від A до F:", bfs(graph, start, goal))
