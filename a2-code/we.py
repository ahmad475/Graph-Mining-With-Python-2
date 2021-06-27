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


fp = open("q2005w.json","w")
json.dump(we,fp, indent=2)

print("")
