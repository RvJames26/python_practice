# lower() converts all characters of the string into lower case. 
# Create a program that does the same functionality without using lower() function.

text = input("Enter text: ")
result = ""

for char in text:
    if 'A' <= char <= 'Z':
        result += chr(ord(char) + 32)
    else:
        result += char

print(result)