#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the lowest number
num_set = []
while True:
    try:
        numbers_given = float(input("Type your numbers: "))
        num_set.append(numbers_given)
    except ValueError:
        lowest_num =  min(num_set)
        print("Invalid Input")
        print(f"Lowest number: {lowest_num}")
        break