# Prog07. zfill() add zero characters at the beginning of the string to complete the number of characters specifies in function parameter.
#  Create a program that do the same functionality without using zfill() function.

text = input("Enter text: ")
width = int(input("Enter total width: "))

if len(text) < width:
    pad_len = width - len(text)
    if text and (text[0] == '+' or text[0] == '-'):
        text = text[0] + ("0" * pad_len) + text[1:]
    else:
        text = ("0" * pad_len) + text

print(text)