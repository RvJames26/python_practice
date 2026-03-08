#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
num_set = {}
input_set = {}
for i in range(0,2):
    numbers = input("Enter number:")
    set(numbers)
    num_set.update(set(numbers))
print(num_set)