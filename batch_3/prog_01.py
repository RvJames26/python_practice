#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
num_set = set()
for i in range(0,10):
    numbers = int(input("Enter number:"))
    num_set.add(numbers)
print(num_set, end=",")
