import networkx as nx
import matplotlib.pyplot as plt
import json
from copy import deepcopy



jf = open("q2005.json","r")
dt = json.load(jf)
nm = []
G=nx.Graph()
for i in dt:
    t = (i[0],i[1])
    #if t[2]==2006 or t[2]==2005:
    nm.append(t)
we=[]

#G.add_edges_from(nm)
w = 0
for i in nm:
    if G.has_edge(i[0],i[1])==True:
        G[i[0]][i[1]]["weight"] = G[i[0]][i[1]]["weight"] + 1
        # if G[i[0]][i[1]]["weight"]>2:
        #     print(G[i[0]][i[1]]["weight"])
        w=w+1
    else:
        G.add_edge(i[0],i[1],weight=1)



print(w)
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
G0 = G.subgraph(Gcc[0])
print(nx.info(G0))

s=nx.algorithms.pagerank(G0)
s1 = sorted(s.items(),key= lambda t: t[1],reverse=True)
#iterator = iter(s1.items())
print("\n")
for i in range(50):
    #print(next(iterator))
    print(s1[i])

print("\n")
print("\n")
x = nx.edge_betweenness_centrality(G0, k=5, normalized=True, weight=None, seed=None)

print("xx\n")
x1 = sorted(x.items(),key= lambda t: t[1],reverse=True)
print("xx\n")
for i in range(20):
    #print(next(iterator))
    print(x1[i])
