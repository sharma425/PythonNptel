import networkx as nx
import matplotlib.pyplot as plt
G = nx.Graph()
"""
G.add_node(1)
G.add_node(2)
G.add_node(3)

G.add_edge(1, 2)
G.add_edge(3, 2)
G.add_edge(1, 3)

print(G.edges())

nx.draw(G)
plt.show()


"""
l=[1,2,3]
#G.add_nodes_from(l)

#G = nx.complete_graph(5)
G = nx.gnp_random_graph(20,0.5)


nx.draw(G)
plt.show()
