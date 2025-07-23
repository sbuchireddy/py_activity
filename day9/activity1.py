dict1={'x':10,'y':20} #input
dict2={'y':99,'z':30}
dict1.update(dict2) #sol1
print(dict1)

#sol2
merged=dict1|dict2
print(merged)

