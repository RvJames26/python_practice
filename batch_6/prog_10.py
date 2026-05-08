# Prog10. title() makes all first letter of each word in the string, capital letter. And all other letter in small case. 
# Create a program that do the same functionality without using title() function.

text = input("Enter text: ")
result = ""
new_word = True # Flag to track if we are at the start of a word

for char in text:
    if char == " ":
        result += char
        new_word = True # The next character will be the start of a new word
    elif new_word:
        # Capitalize if it's the start of a word
        if 'a' <= char <= 'z':
            result += chr(ord(char) - 32)
        else:
            result += char
        new_word = False # Turn off flag until we hit another space
    else:
        # Lowercase if it's in the middle of a word
        if 'A' <= char <= 'Z':
            result += chr(ord(char) + 32)
        else:
            result += char

print(result)