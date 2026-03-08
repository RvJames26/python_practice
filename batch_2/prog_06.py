#Create a program that ask user to input 10 numbers. Print the result of the first number minus all of the remaining numbers.
first_num = float(input("First number:"))
for i in range(1,10):
    remaining_num = float(input("Enter number:"))
    print(first_num - remaining_num)