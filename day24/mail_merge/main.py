#!/user/bin/env python

# Objective:
# Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

with open("Input/Letters/starting_letter.txt") as f:
    form_letter = f.read()

with open("Input/Names/invited_names.txt") as f:
    names = f.readlines()

for name in names:
    name = name.replace("\n", "")
    new_letter = form_letter.replace("[name]", name)
    name = name.replace(" ", "-")
    file_name = f"letter_for_{name}.txt"
    with open(f"Output/ReadyToSend/{file_name}", "w") as f:
        f.write(new_letter)
