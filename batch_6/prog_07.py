# Prog07. center() add space characters at the beginning and at the end of the string to print the string at the center. 
# Create a program that do the same functionality without using center() function.

text = input("Enter text: ")
width = int(input("Enter total width: "))

if len(text) < width:
    total_padding = width - len(text)
    # Integer division to get half for the left
    left_pad = total_padding // 2 
    # Subtract left from total to get the remainder for the right
    right_pad = total_padding - left_pad 
    
    text = (" " * left_pad) + text + (" " * right_pad)

# Quotes added to the print statement so you can see the spaces
print(f"'{text}'")