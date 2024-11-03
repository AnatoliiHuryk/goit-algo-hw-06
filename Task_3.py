import networkx as nx
import matplotlib.pyplot as plt
import heapq

G_weighted = nx.Graph()
weighted_edges = [
    ('A', 'B', 4), ('A', 'C', 2), ('B', 'D', 5), ('C', 'D', 8), 
    ('C', 'E', 10), ('D', 'E', 2), ('D', 'F', 6), ('E', 'F', 3)
]
G_weighted.add_weighted_edges_from(weighted_edges)

# Aлгоритм Дейкстри
def dijkstra(graph, start, goal):
    queue = [(0, start, [])]
    visited = set()
    while queue:
        (cost, node, path) = heapq.heappop(queue)
        if node in visited:
            continue
        path = path + [node]
        if node == goal:
            return (cost, path)
        visited.add(node)
        for neighbor, edge_data in graph[node].items():
            if neighbor not in visited:
                heapq.heappush(queue, (cost + edge_data['weight'], neighbor, path))
    return float("inf"), []

start, goal = 'A', 'F'
shortest_path_cost, shortest_path = dijkstra(G_weighted, start, goal)
print(f"Найкоротший шлях Дейкстри від {start} до {goal}: {shortest_path} з вартістю {shortest_path_cost}")

pos = nx.spring_layout(G_weighted)
nx.draw(G_weighted, pos, with_labels=True, node_color='lightgreen', node_size=2000, font_size=16)
edge_labels = nx.get_edge_attributes(G_weighted, 'weight')
nx.draw_networkx_edge_labels(G_weighted, pos, edge_labels=edge_labels)
plt.title("Зважений граф для алгоритму Дейкстри")
plt.show()
