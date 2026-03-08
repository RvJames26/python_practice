#Create a program that print all the odd numbers starting from 0 to 100. (Use while loop)
number = 0
for i in range(1,101):
    number += 1
    if i % 2 == 1:
        print(number,end=",")
    if i % 2 == 0:
        continue