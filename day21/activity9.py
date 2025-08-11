import os
'''
path="project/assets/images"
os.makedirs(path, exist_ok=True)
'''
import os
path = os.path.join("project", "assets", "images")
os.makedirs(path, exist_ok=True)
print(f"Directory structure '{path}' created successfully!")
