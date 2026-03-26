# Example 1 - Create file and write text
with open("example1.txt", "w") as f:
    f.write("Hello World\n")

# Example 2 - Write multiple lines
with open("example2.txt", "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
    f.write("Line 3\n")

# Example 3 - Write list to file
lines = ["Apple\n", "Banana\n", "Orange\n"]
with open("example3.txt", "w") as f:
    f.writelines(lines)

# Example 4 - Write numbers
with open("example4.txt", "w") as f:
    for i in range(1,6):
        f.write(str(i) + "\n")

# Example 5 - Write user input
text = "Python practice"
with open("example5.txt", "w") as f:
    f.write(text)