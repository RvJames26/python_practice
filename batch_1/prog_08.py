#Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd_count = 0
for i in range (0,10):
    numbers = float(input("Enter number:"))
    if numbers % 2 == 1:
        odd_count += 1
    if numbers % 2 == 0:
        odd_count += 0
print(f"Odd count: {odd_count}")