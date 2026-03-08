#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
numbers = []
for i in range(0,10):
    numbers = float(input("Enter number:"))
    if numbers != numbers:
        print(numbers)
    if numbers == numbers:
        continue
