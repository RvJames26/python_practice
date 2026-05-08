# Prog01. rstrip() remove the space characters at the end of the string. Create a program that do the same functionality without using rstrip() function.

text = input("Enter text: ")

end_idx = len(text)
while end_idx > 0 and text[end_idx - 1] == ' ':
    end_idx -= 1

result = text[:end_idx]

print(f"'{result}'")