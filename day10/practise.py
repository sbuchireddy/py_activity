s1={1,2,3}
id(s1)
1837415981888
type(s1)
<class 'set'>
s2=set([1,2,3])
type(s2)
<class 'set'>
id(s1)
1837415981888
id(s2)
1837415981440
s={1,2,[3,4],"hello"}
TypeError: unhashable type: 'list'
s3=(1,2,[3,4],"hello")
s3
s={1,2,(True)}
s
s={1,2,(3,4),True}
s
s={1,2,[3,4],True}
s={1,2,[3,4],"True"}
TypeError: unhashable type: 'list'
s={1,2,"True"}
s
s={True}
s
s={1>0}
s
s={1,2,{3,4}}
TypeError: unhashable type: 'set'
s={1,2,{3:"alice"}}
TypeError: unhashable type: 'dict'
s={2,True}
s
{True, 2}
{1,true}

word=set('programming')
print(len(word))
8

fruits={'apple','banana'}

fruits.add('orange') #adding elements
print(fruits)
fruits.update(['grape','mango']) #update
fruits.remove #remove
fruits.update #update
fruits.pop() #pop
fruits.clear() #clear

colors={'red','green','blue'}
cond={'red' in colors,'yellow' not in colors}
print(cond)

x = True
y = False
result = x and y 
print(result)

a = 5 
b = 3 
result = a & b
print(result)

set1={1,2,3}
set2={3,4,5}
result=set1|set2  #union operator
result=set1&set2 #intersection operator