my_list = [10, 20, 30, 40, 50]
 
index_to_access = 2 
 
try:
    element = my_list[index_to_access]
    print(f"{element} Found")
except IndexError:
	print("Out of bounds")