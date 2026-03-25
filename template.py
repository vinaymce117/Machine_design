import os

# List of directories to create
directories = [
    "research",
    "src",
    "data"
]

# List of files to create
files = [
    "src/__init__.py",
    "src/helper.py",
    "src/prompt.py",
    ".env",
    "setup.py",
    "app.py",
    "research/trails.ipynb",
    "requirements.txt",
]

# Create directories
for directory in directories:
    os.makedirs(directory, exist_ok=True)

# Create files
for file in files:
    dir_name = os.path.dirname(file)
    
    # Only create directory if it's not empty
    if dir_name:
        os.makedirs(dir_name, exist_ok=True)
    
    with open(file, "w") as f:
        pass

print("✅ Project structure created successfully!")