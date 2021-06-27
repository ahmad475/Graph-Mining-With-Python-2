import networkx as nx
import matplotlib.pyplot as plt
import json

options = {

    'node_color': 'red',

    'node_size': 20,

    'width': 0.1,

   # 'with_labels':True,

    'font_size':5,


}


jf = open("q2006.json","r")
dt = json.load(jf)
nm = []
G=nx.Graph()

print("y1\n")
for i in dt:
    t = (i[0],i[1])
    #if t[2]==2006 or t[2]==2005:
    nm.append(t)
#    print(t)
print("y2\n")
G.add_edges_from(nm)
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
G0 = G.subgraph(Gcc[0])
print("y3\n")
#nx.draw(G0,**options)
print("y4\n")
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
