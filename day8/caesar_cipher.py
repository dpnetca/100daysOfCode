import art

alphabet = [
    "a",
    "b",
    "c",
    "d",
    "e",
    "f",
    "g",
    "h",
    "i",
    "j",
    "k",
    "l",
    "m",
    "n",
    "o",
    "p",
    "q",
    "r",
    "s",
    "t",
    "u",
    "v",
    "w",
    "x",
    "y",
    "z",
]


# oops probably supposed to use letter list, not ord/chr...
# def text_shift(text, shift):
#     shift_text = ""
#     shift = shift % 26
#     for letter in text:
#         shifted_ord = ord(letter) + shift
#         if shifted_ord > 122:
#             shifted_char = chr(shifted_ord - 26)
#         else:
#             shifted_char = chr(shifted_ord)

#         shift_text += shifted_char
#     return shift_text


def text_shift(text, shift):
    shift_text = ""
    normalized_shift = shift % len(alphabet)
    for letter in text:
        if letter in alphabet:
            position = alphabet.index(letter)
            new_position = position + normalized_shift
            if new_position >= len(alphabet):
                new_position -= len(alphabet)
            shift_text += alphabet[new_position]
        else:
            shift_text += letter
    return shift_text


# def encrypt(text, shift):
#     cipher_text = text_shift(text, shift)
#     print(f"the encoded text is {cipher_text}")


# def decrypt(cipher_text, shift):
#     shift *= -1
#     text = text_shift(cipher_text, shift)
#     print(f"the decoded text is {text}")


def caesar(text, shift, direction):
    if direction.lower() == "decode":
        shift *= -1
    elif direction.lower() == "encode":
        pass
    else:
        print("invalid selection")
        return
    new_text = text_shift(text, shift)
    print(f"Your {direction}d message is {new_text}")


print(art.logo)


run_again = True
while run_again:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    direciton = direction.lower()
    if direction in ["encode", "decode"]:
        text = input("Type your message:\n").lower()
        shift = int(input("Type the shift number:\n"))
        caesar(text, shift, direction)
    else:
        print("invalid entry, try again")

    again = input("run again 'yes' or 'no'? ").lower()
    if again == "no":
        run_again = False
    elif again == "yes":
        continue
    else:
        print("invalid entry...lets go again anyway")
