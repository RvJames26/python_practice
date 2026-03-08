#Create a program that ask user to input 10 numbers. Print how many are even numbers.
even_count = 0
for i in range (0,10):
    numbers = float(input("Enter number:"))
    if numbers % 2 == 1:
        even_count += 0
    if numbers % 2 == 0:
        even_count += 1
print(f"Even count: {even_count}")