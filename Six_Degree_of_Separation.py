import networkx as nx
import numpy 
G = nx.read_edgelist("facebook_combined.txt")
N = list(G.nodes())
spll = []

for u in N:
    for v in N:
        if u!=v:
            l=nx.shortest_path_length(G,u,v)
            print("Shortest Path between ",u,"and",v,"is of length : ",l)
            spll.append(1)
            
            
min_spl=min(spll)
max_spl = max(spll)
avg_spl = numpy.average(spll)
print("Minimum shortest path length :",min_spl)
print("Maximum shortest path length :",max_spl)
print("Average shortest path length :",avg_spl)