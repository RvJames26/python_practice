# removeprefix() removes the characters at the beginning of the string that matches the function parameter. 
# Create a program that does the same functionality without using removeprefix() function.

text = input("Enter text: ")
prefix = input("Enter prefix: ")

if prefix and text.startswith(prefix):
    text = text[len(prefix):]

print(text)