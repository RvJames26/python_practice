#Create a program that ask user to input 10 numbers. Display all numbers that don't have duplicate.
num_set = []
final_number = []
for i in range(0,10):
    numbers = int(input("Enter number:"))
    final_number.append(numbers)
for i in final_number:
    if final_number.count(i) >= 1:
        print(i, end=",")
        continue
print(num_set)