
# isupper() checks if all characters of the string are in upper case. 
# Create a program that does the same functionality without using isupper() function.

text = input("Enter text: ")

has_upper = False
has_lower = False

for char in text:
    # Check if the character is lowercase
    if 'a' <= char <= 'z':
        has_lower = True
    # Check if the character is uppercase
    elif 'A' <= char <= 'Z':
        has_upper = True

# Python's isupper() only returns True if there is at least ONE uppercase letter
# and absolutely NO lowercase letters. (Numbers and symbols are ignored).
if has_upper and not has_lower:
    print(True)
else:
    print(False)
