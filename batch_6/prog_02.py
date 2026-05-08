text = input("Enter the text: ")
prefix = input("Enter the prefix to remove: ")

if prefix and text.startswith(prefix):
    text = text[len(prefix):]

print(text)