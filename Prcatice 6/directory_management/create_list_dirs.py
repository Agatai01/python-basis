import os

# Example 1 - Create directory
os.mkdir("folder1")

# Example 2 - Create nested directories
os.makedirs("folder2/subfolder", exist_ok=True)

# Example 3 - List files
print(os.listdir("."))

# Example 4 - Check directory exists
print(os.path.isdir("folder1"))

# Example 5 - Get current directory
print(os.getcwd())