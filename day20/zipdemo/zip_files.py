import zipfile
'''
with zipfile.ZipFile('archive.zip',mode='w')as zf:
	zf.write('file1.txt')
	zf.write('file2.txt')
	zf.write('file3.txt')
'''
'''
with zipfile.ZipFile('archeive.zip','w', compression=zipfile.ZIP_DEFLATED) as zipf:
	zipf.write('report.txt')
	zipf.write('summary.txt')
'''
'''
with zipfile.ZipFile('archive.zip','r') as zipf:
	zipf.extractall('extracted_files')
'''

with zipfile.ZipFile('archive.zip','r') as zipf:
	print("files in archive:",zipf.namelist())
	info=zipf.getinfo('file1.txt')
	print("Compressed size:",info.compress_size,"bytes")
	print("originalsize:",info.file_size,"bytes")
	print("date:",info.date_time)



'''
for i in range(1, 4):
	with open(f"file{i}.txt", "w") as f:
 		f.write(f"Hello from file {i}!")
with zipfile.ZipFile("activity2.zip", "w") as z:
	for i in range(1, 4):
		z.write(f"file{i}.txt")
with zipfile.ZipFile("activity2.zip", "r") as z:
	z.extractall("extracted_files")
	print("Files in ZIP:", 
	*z.namelist(), sep="\n- ")
'''