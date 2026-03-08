#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
num_entered = []
duplicates = []
for i in range(0,2):
    numbers = (input("Enter number:"))
    if numbers in num_entered:
        numbers.append(num_entered)
print(num_entered)