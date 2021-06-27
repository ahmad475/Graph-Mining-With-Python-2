import networkx as nx
import json
import time


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
Gcc = sorted(nx.connected_components(G), key=len, reverse=True)
G0 = G.subgraph(Gcc[0])
t=0


###########################2005remove nodes d<3 from graph############################################
print("i: Beginning where 2005 d>=3")
G1=nx.Graph(G0)
print(nx.info(G1))
remn = []
for i in G1.nodes():
    if G1.degree(i)<3:
        # print(t)
        # print(i)
        remn.append(i)

G1.remove_nodes_from(remn)
print(nx.info(G1))

###########################2006create graph giant component############################################
print("dblp2006: created and Giant component obtained")
jf2 = open("q2006.json","r")
dt2 = json.load(jf2)
nm2 = []
G2=nx.Graph()

for i in dt2:
    t2 = (i[0],i[1])
    #if t[2]==2006 or t[2]==2005:
    nm2.append(t2)


G2.add_edges_from(nm2)
Gcc2 = sorted(nx.connected_components(G2), key=len, reverse=True)
G02 = G2.subgraph(Gcc2[0])
t=0
###########################2006remove nodes d<3 from graph############################################
print("ii: Beginning where 2006 d>=3 2006 obtained")
G12=nx.Graph(G02)
print(nx.info(G12))
remn2 = []
for i in G12.nodes():
    if G12.degree(i)<3:
        # print(t)
        # print(i)
        remn2.append(i)

G12.remove_nodes_from(remn)
print(nx.info(G12))

###########################2005 FoF###################################################################
print("iii:Beginning FoF is being obtained")
twohops = []
#print(nx.is_frozen(G1))
twos=dict(nx.all_pairs_shortest_path(G1, cutoff=2))
#ones=twos=dict(nx.all_pairs_shortest_path(G1, cutoff=1))
fofs=[]
for i in twos:
    # print(i)
    # print("/////////////////////////")
    # print(twos[i])
    for q in twos[i]:
        # print(q)
        # print(twos[i][q])
        # print(len(twos[i][q]))
        if len(twos[i][q])>2:
            tup=(i,q)
            fofs.append(tup)
    # print("/////////////////////////")

print(len(fofs))
###########################t in 2006 not in 2005###################################################################
print("iv: Beginning get all in 2006 and not in 2005")
t1=[]
co=0
for i in G12.edges:
    if G1.has_edge(i[0],i[1])==False:
        # print(i)
        # co=co+1
        # print("true exists")
        t1.append(i)
        # print(co)

qq=0
qq=len(t1)
print(qq)

########################Computer predicted Edges P according to Link Prediction###################################
###################a. RD: random predictor#######################
print("v a.: LINK PREDICTION")
time2 = time.strftime('%H:%M:%S')
#x=nx.jaccard_coefficient(G1, ebunch=fofs)
#x=nx.preferential_attachment(G1,ebunch=fofs)
#x=nx.adamic_adar_index(G1, ebunch=fofs)










res=[]
print(time2)
c=0
for i in fofs:
    c=c+1
    res.append(i)

print("PREDICTION ALGORITHMS NOW:")





top10=0
top20=0
top50=0
top100=0
topt=0
topqq=0
res.sort(key=lambda res:res[2], reverse=True)
print("done checking precision now:")


for i in range(10):
    w=res[i]
    if ((w[0],w[1]) in t1) or ((w[1],w[0]) in t1):
        top10=top10+1
Pat10=top10/10
print("P@10 is", Pat10)




for i in range(20):
    #print(res[i])
    w=res[i]
    if ((w[0],w[1]) in t1) or ((w[1],w[0]) in t1):
        top20=top20+1
Pat20=top20/20
print("P@20 is", Pat20)






for i in range(50):
    w=res[i]
    if ((w[0],w[1]) in t1) or ((w[1],w[0]) in t1):
        top50=top50+1
Pat50=top50/50
print("P@50 is", Pat50)


for i in range(100):
    w=res[i]
    if ((w[0],w[1]) in t1) or ((w[1],w[0]) in t1):
        top100=top100+1
Pat100=top100/100
print("P@100 is", Pat100)

for i in range(qq):
    w=res[i]
    if G12.has_edge(w[0],w[1]):
        topqq=topqq+1
        # print(topqq)
        # print(i)
Patqq=topqq/qq
print("P@qq is", Patqq)
















print(c)
print(time.strftime('%H:%M:%S'))
