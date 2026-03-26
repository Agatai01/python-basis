import shutil

# Example 1 - Move file
shutil.move("example1.txt", "folder1/example1.txt")

# Example 2 - Move file back
shutil.move("folder1/example1.txt", "example1.txt")

# Example 3 - Copy file to folder
shutil.copy("example2.txt", "folder1/")

# Example 4 - Copy folder
shutil.copytree("folder1", "folder1_backup", dirs_exist_ok=True)

# Example 5 - Move folder
shutil.move("folder1_backup", "folder_backup")