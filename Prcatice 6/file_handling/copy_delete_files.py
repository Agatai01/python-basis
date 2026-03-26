import shutil
import os

# Example 1 - Copy file
shutil.copy("example1.txt", "copy1.txt")

# Example 2 - Copy with metadata
shutil.copy2("example2.txt", "copy2.txt")

# Example 3 - Rename file
os.rename("copy1.txt", "renamed_copy.txt")

# Example 4 - Check if file exists
print(os.path.exists("example3.txt"))

# Example 5 - Delete file
if os.path.exists("copy2.txt"):
    os.remove("copy2.txt")