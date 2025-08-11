with zipfile.ZipFile('archive.zip', mode='') as zf:
	zf.write('file1.txt')
	zf.write('file2.txt')
	zf.write('file3.txt')