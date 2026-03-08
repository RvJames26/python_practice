#Create a program that ask user to input 2 numbers. Print the bigger number.
num_01 = float(input("Input your first number: "))
num_02 = float(input("Input your second number: "))
if num_01 > num_02:
    print(f"{num_01} is greater than {num_02}.")
if num_02 > num_01:
    print(f"{num_02} is greater than {num_01}.")
if num_01 == num_02:
    print(f"{num_01} and {num_02} is equal.")