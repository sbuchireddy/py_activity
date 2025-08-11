'''
file_handle = open('hello.txt','r')
if:
	content=file_handle.read()
	print(content)
file_handle.close()
'''

try:
	file_handle = open('hello.txt','r')
except Exception as err:
	print(f"Error: {err}\nType:{type(err)}")
else:
	content=file_handle.read()
	print(type(content))
	file_handle.close()
finally:
	print("file closed")