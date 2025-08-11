import zipfile
zip_path = input("enter the path")
with zipfile.ZipFile(archive.zip,'r') as zipf:
	if 'foo.txt' in zipf.namelist():
		print("found!")
	else:
		print("missing!")