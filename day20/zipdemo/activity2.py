import zipfile
'''
with zipfile.ZipFile('activity2.zip',mode='w')as zf:
	zf.write('file1.txt')
	zf.write('file2.txt')
	zf.write('file3.txt')
'''

for i in range(1, 4):
	with open(f"file{i}.txt", "w") as zf:
 		zf.write(f"Hello from file {i}!")
with zipfile.ZipFile("activity2.zip", "w") as zipf:
	for i in range(1, 4):
		zipf.write(f"file{i}.txt")
with zipfile.ZipFile("activity2.zip", "r") as zipf:
	zipf.extractall("extracted_files")
	print("Files in ZIP:", 
	*zipf.namelist(), sep="\n- ")

