import pandas

# Loop through rows of a data frame
# for (index, row) in student_data_frame.iterrows():
# Access index and row
# Access row.student or row.score
# pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

# Create a dictionary in this format:
# {"A": "Alfa", "B": "Bravo"}
df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for _, row in df.iterrows()}


# Create a list of the phonetic code words from a word that the
# user inputs.
user_input = input("input string: ")

# nato_string = [nato_dict[letter.upper()] for letter in user_input]

# # add a bit of error checking:
# nato_string = [
#     nato_dict[letter.upper()]
#     for letter in user_input
#     if letter.upper() in nato_dict.keys()
# ]
# # or
nato_string = [nato_dict.get(letter.upper(), letter) for letter in user_input]

print(nato_string)
