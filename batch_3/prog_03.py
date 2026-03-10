#Create a program that ask user to input a number, continue asking until the user input is invalid.
#Display "Unique" after input when the inputted number don't have duplicate. 
# Display "Duplicate" after input when the inputted number have duplicate.
num_set = []
final_number = []
for i in range(0,10):
    numbers = int(input("Enter number:"))
    final_number.append(numbers)
if final_number.count(i) == 1:
    print("Unique")
if final_number.count(i) < 1:
    print("Duplicate")