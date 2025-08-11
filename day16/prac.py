'''
def main_f():
	def sub_f():
		return "Hello"
	return sub_f
ret=main_f()
print(ret())
'''
def extend_list(val,lst=[]):
     lst +=[val]
     return lst
a= print(extend_list(1)) #1 is added to list
b= print(extend_list(2,[])) #2 is added to val
c= print(extend_list(3))#3 is added to the list along with 1-[1,3]
d= print(extend_list(4))#4 is added to list so now [1,3,4]
print(id(a),a)
print(id(b),b)
print(id(c),c)
print(id(d),d)