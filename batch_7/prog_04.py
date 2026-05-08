# Prog04. islower() check if all characters of the string is on lower case.
#  Create a program that do the same functionality without using islower() function.

text = input("Enter text: ")

has_lower = False
has_upper = False

for char in text:
    if 'a' <= char <= 'z':
        has_lower = True
    elif 'A' <= char <= 'Z':
        has_upper = True

if has_lower and not has_upper:
    print(True)
else:
    print(False)