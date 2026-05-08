# Prog06. rjust() add space characters at the beginning of the string to complete the number of characters specifies in function parameter. Create a program that do the same functionality without using rjust() function.

text = input("Enter text: ")
width = int(input("Enter total width: "))

if len(text) < width:
    text = (" " * (width - len(text))) + text

print(f"'{text}'")