# Prog09. index() return the first location of the function parameter in the string.
#  Create a program that do the same functionality without using index() function.

text = input("Enter text: ")
sub = input("Enter substring to find: ")
found_idx = -1

if not sub:
    found_idx = 0
else:
    for i in range(len(text) - len(sub) + 1):
        if text[i:i+len(sub)] == sub:
            found_idx = i
            break 

if found_idx != -1:
    print(found_idx)
else:
    print("ValueError: substring not found")