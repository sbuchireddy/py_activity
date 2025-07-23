d={"a":1,"b":2}
keys=d.keys()
d["c"]=3
print(len(keys))

players={1:"dhoni",2:"kholi",3:"rohith"}
del players[3]
print(players)
players={1:"dhoni",2:"kholi",3:"rohith"}
players.pop(3)
print(players)

players={1:"dhoni",2:"kholi",3:"rohith"}
print(1 in players)
print(3 not in players)

a=[{"amit":{"math":95}}]
print(a)

student={"Amit":{"Math":95,"Science":89},"Ravi":{"Math":80,\"Science":92},}
print(student["Ravi"])
print(student["Ravi"]["Science"])

employee={"name":"john","age":22,"salary":32000}
print(len(employee))
mployee.clear()
print(employee)

d={'x':10}
values=d.values()
d['y']=20
print(list(values))

dict1={"name":"Ravi","age":25}
dict2={"age":30,"city":"Chennai"}
dict1|dict2

d={'one':1,'two':2}
x=d.pop('three',-1)
x
d.popitem()
print(d)