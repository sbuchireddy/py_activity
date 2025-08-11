import os
cwd = os.getcwd()
items = os.listdir(cwd)
count = len(items)
print(f"Total items in '{cwd}': {count}")
