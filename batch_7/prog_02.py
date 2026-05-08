# Prog02. removesuffix() remove the characters at the end of the string that matches the function parameter. Create a program that do the same functionality without using removesuffix() function.

text = input("Enter text: ")
suffix = input("Enter suffix to remove: ")

if suffix and len(text) >= len(suffix) and text[-len(suffix):] == suffix:
    text = text[:-len(suffix)]

print(text)