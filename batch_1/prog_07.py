#Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
start = 0
for i in range (0,10):
    numbers = float(input("Enter number:")) 
    start += numbers
    print(start)