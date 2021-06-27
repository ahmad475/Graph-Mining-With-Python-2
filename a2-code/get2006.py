import networkx as nx
import json


jf = open("tmp_dblp_coauthorship.json","r")
dt = json.load(jf)
nm = []
print(dt[3][2])
dt2= []
for i in dt:
    if i[2]==2006:
        dt2.append(i)

fp = open("q2006.json","w")
json.dump(dt2,fp, indent=2)








# for i in dt:
#     if i[2]==2006 or i[2]==2005:
#         print(i)
#         json.dump(i,fp)
# for i in dt:
#     t= tuple(i)
#     if t[2]==2006 or t[2]==2005:
#         nm.append(t)
#         print(t)
