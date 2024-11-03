import networkx as nx
import matplotlib.pyplot as plt

G = nx.Graph()

nodes = ['A', 'B', 'C', 'D', 'E', 'F']
G.add_nodes_from(nodes)

# Додаємо ребра (наприклад, дороги або маршрути) між вершинами
edges = [
    ('A', 'B'), ('A', 'C'), ('B', 'D'), ('C', 'D'), 
    ('C', 'E'), ('D', 'E'), ('D', 'F'), ('E', 'F')
]
G.add_edges_from(edges)

# Візуалізуємо граф
nx.draw(G, with_labels=True, node_color='lightblue', edge_color='gray', node_size=2000, font_size=16)
plt.title("Транспортна мережа")
plt.show()

# Аналіз основних характеристик графу
print("Кількість вершин:", G.number_of_nodes())
print("Кількість ребер:", G.number_of_edges())
print("Ступені вершин:", dict(G.degree()))
