# Take a look inside file1.txt and file2.txt.
# They each contain a bunch of numbers, each number on a new line.
# You are going to create a list called result which contains the numbers
# that are common in both files.

with open("file1.txt") as f:
    file1_list = f.readlines()

with open("file2.txt") as f:
    file2_list = f.readlines()

result = [int(n.strip()) for n in file1_list if n in file2_list]

# Write your code above 👆


print(result)
