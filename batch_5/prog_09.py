# Create a program that ask the user to input their fullname in incorrect casing.
#  Print the input in pascal case.
# Example:
# Input: jUAn DEla CrUZ
# Output: JuanDelaCruz

name_incorrect = input("Input your name(incorrect casing): ")
name_lower = name_incorrect.lower()
name_title = name_lower.title()
no_space = name_title.replace(" ", "")
print(no_space)
