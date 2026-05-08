# Prog06. ljust() add space characters at the end of the string to complete the number of characters specifies in function parameter. 
# Create a program that do the same functionality without using ljust() function.

text = input("Enter text: ")
width = int(input("Enter total width: "))

if len(text) < width:
    # Multiply space character by the remaining width needed
    text = text + (" " * (width - len(text)))

# Quotes added to the print statement so you can see the trailing spaces
print(f"'{text}'")