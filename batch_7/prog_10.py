# Prog10. rindex() return the first location of the function parameter in the string starting from the last character. Create a program that do the same functionality without using rindex() function.

text = input("Enter text: ")
sub = input("Enter substring to find: ")
found_idx = -1

if not sub:
    found_idx = len(text)
else:
    for i in range(len(text) - len(sub), -1, -1):
        if text[i:i+len(sub)] == sub:
            found_idx = i
            break 

if found_idx != -1:
    print(found_idx)
else:
    print("ValueError: substring not found")