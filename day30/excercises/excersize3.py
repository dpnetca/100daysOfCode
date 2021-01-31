import pandas

df = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_dict = {row.letter: row.code for _, row in df.iterrows()}

valid_input = False
while not valid_input:
    user_input = input("input string: ")
    try:
        nato_string = [nato_dict[letter.upper()] for letter in user_input]
    except KeyError:
        print("Sorry only letters in the alphabet please")
    else:
        valid_input = True

print(nato_string)
