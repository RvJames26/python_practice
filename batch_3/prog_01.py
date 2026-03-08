#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
num_set = []
unique_set = []
for i in range(0,2):
    numbers = int(input("Enter number:"))
    num_set.append(numbers)
for num in num_set:
    if num_set.count(num) == 1:
        num_set.append(unique_set)
print(unique_set)