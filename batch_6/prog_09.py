# Prog09. capitalize() makes the first letter of the string, capital letter. And all other letter in small case. 
# Create a program that do the same functionality without using capitalize() function.

text = input("Enter text: ")
result = ""

for i in range(len(text)):
    char = text[i]
    # For the very first character
    if i == 0:
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
    # For all subsequent characters
    else:
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char

print(result)