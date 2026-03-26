# Example 1 - Read full file
with open("example1.txt", "r") as f:
    print(f.read())

# Example 2 - Read line by line
with open("example2.txt", "r") as f:
    for line in f:
        print(line.strip())

# Example 3 - Read lines as list
with open("example3.txt", "r") as f:
    lines = f.readlines()
print(lines)

# Example 4 - Read first line
with open("example2.txt", "r") as f:
    print(f.readline())

# Example 5 - Count lines
with open("example4.txt", "r") as f:
    count = len(f.readlines())
print("Number of lines:", count)