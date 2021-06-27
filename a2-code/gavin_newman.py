import itertools
import networkx as nx
from networkx.algorithms.community.centrality import girvan_newman
import json
###########################2005create graph giant component############################################
print("dblp2005: created and Giant component obtained")
jf = open("q2005.json","r")
dt = json.load(jf)
nm = []
G=nx.Graph()


for i in dt:
    t = (i[0],i[1])
    #if t[2]==2006 or t[2]==2005:
    nm.append(t)

G.add_edges_from(nm)




G1=nx.Graph(G)
print(nx.info(G1))
remn = []
for i in G1.nodes():
    if G1.degree(i)<30:
        # print(t)
        # print(i)
        remn.append(i)

G1.remove_nodes_from(remn)

Gcc = sorted(nx.connected_components(G1), key=len, reverse=True)
G0 = G1.subgraph(Gcc[0])
print(nx.info(G0))


coml=[]


limited = itertools.takewhile(lambda c: len(c) <= 10, nx.algorithms.community.centrality.girvan_newman(G0) )
for communities in limited:
    #print(tuple(sorted(c) for c in communities))

    q=tuple(sorted(c) for c in communities)
    print(len(q))
    for i in q:
        print("//"+str(len(i)))
        for p in i:
            coml.append(len(p))
            #print("////"+str(len(p)))
    print("\n\n\n")



coml.sort(key=lambda coml:coml, reverse=True)
for i in range(10):
    print(coml[i])
