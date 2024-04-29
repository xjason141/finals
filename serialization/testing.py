import os

nlist=[]

for stuff in os.listdir('serialization'):
    # print(stuff)
    nlist.append(stuff)

print(nlist)
print(type(nlist))
