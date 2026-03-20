# Create a program that ask the user to input their fullname in incorrect casing. Print the input in proper casing.
# Example:
# Input: jUAn DEla CrUZ
# Output: Juan Dela Cruz

name = input("Please input your full name: ")
upper_case = name.title()
print(upper_case)