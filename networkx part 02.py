# Go to networkx documents -> Graph generator
import networkx as nx
import matplotlib.pyplot as plt
#G = nx.gnp_random_graph(50,0.3)
G = nx.barabasi_albert_graph(50,2)  # scale free graph
nx.draw(G)
plt.show()


nx.write_gexf(G,"analysis.gexf")
print("done")

#print(G.nodes())
#print(G.edges())
#print(G.degree(0))
