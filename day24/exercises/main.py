#!/usr/bin/env python

# default opens for read only
# with open("my_file.txt") as file:
#     content = file.read()

# print(content)

# append to end of file
# with open("my_file.txt", "a") as file:
#     file.write("\nNew text.")

# new_file doesn't exist will be created
# with open("new_file.txt", "w") as file:
#     file.write("\nNew text.")

# open with absolute path
# with open("/home/denis/100days/day24/exercises/my_file.txt") as file:
#     content = file.read()
# print(content)

# open with a relative file path
with open("../../day24/exercises/my_file.txt") as file:
    content = file.read()
print(content)
