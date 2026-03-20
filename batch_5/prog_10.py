# Prog10: Create a program that ask the user to input their fullname in 
# incorrect casing. Print the input in snake case.
# Example:
# Input: jUAn DEla CrUZ
# Output: juan_dela_cruz

name_incorrect = input("Input your name(incorrect casing): ")
name_lower = name_incorrect.lower()
snake_case = name_lower.replace(" ", "_")
print(snake_case)
