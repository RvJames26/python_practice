#Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
num_01 = float(input("Input your first number: "))
num_02 = float(input("Input your second number: "))
if num_01 == num_02:
    print(f"Equal")
if num_01 != num_02:
    print(f"Not Equal")