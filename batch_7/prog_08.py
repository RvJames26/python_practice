# Prog08. count() return how many time the function parameter appear in the string. 
# Create a program that do the same functionality without using count() function.

text = input("Enter text: ")
sub = input("Enter substring to count: ")
count = 0

if not sub:
    count = len(text) + 1
else:
    i = 0
    while i <= len(text) - len(sub):
        if text[i:i+len(sub)] == sub:
            count += 1
            i += len(sub)
        else:
            i += 1

print(count)