#  Create a program that ask the user to input a complete statement.
#  Print the number of words in the input.
# Example:
# Input: We will weather the weather whatever the weather whether we like it or not
# Output: 14

statement = input("Enter ypur statement: ")

words = statement.split()
count = len(words)

print(f"Number of words: {count}")