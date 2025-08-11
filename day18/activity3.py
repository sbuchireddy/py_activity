data = [('Alice', 90), ('Bob', 75), ('Charlie', 90), ('Dave', 60)] #input

sorted_data = sorted(data, key=lambda x: (-x[1], x[0]))
#sorted data is reveresed with -x
#x[0] sorting alphabetically

print(sorted_data)
