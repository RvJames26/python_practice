#Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
number = 0
for i in range(1,101):
    number += 1
    if number % 2 == 0:
        print(number, end=",")
    if number % 2 == 1:
        continue