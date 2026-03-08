#Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
numbers = 0
for i in range(1,101):
    numbers += 1
    if numbers % 10 == 0:
        continue
    else:
        print(numbers, end=",")