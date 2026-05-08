# Prog05. startswith() check if the string beginning part matches the function parameter. Create a program that do the same functionality without using startswith() function.

text = input("Enter text: ")
prefix = input("Enter prefix to check: ")

if not prefix:
    print(True)
elif len(text) >= len(prefix) and text[:len(prefix)] == prefix:
    print(True)
else:
    print(False)