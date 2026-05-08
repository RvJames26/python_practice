# Prog08. swapcase() reverse the casing of each of the character of the string. 
# Create a program that do the same functionality without using swapcase() function.

text = input("Enter text: ")
result = ""

for char in text:
    # If lowercase, convert to uppercase using ASCII values
    if 'a' <= char <= 'z':
        result += chr(ord(char) - 32)
    # If uppercase, convert to lowercase using ASCII values
    elif 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    # If it's a number or symbol, leave it alone
    else:
        result += char

print(result)