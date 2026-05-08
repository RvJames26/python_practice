# Prog01. lstrip() remove the space characters at the beginning of the string.
# Create a program that do the same functionality without using lstrip() function.

string = input("Enter something: ")

index = 0
while index < len(string) and string[index] == " ":
    index += 1

result = string[index:]
print(result)

