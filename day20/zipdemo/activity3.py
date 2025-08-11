import zipfile

files = ['f1.txt', 'f2.txt', 'f3.txt']

with zipfile.ZipFile('compressed_bzip2.zip', mode='w', compression=zipfile.ZIP_BZIP2) as zipf:
    for file in files:
        zipf.write(file)
        info = zipf.getinfo(file)
        print(f"{info.filename} - {info.compress_size} bytes")