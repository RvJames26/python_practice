#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the highest number
num_set = []
while True:
    try:
        numbers_given = float(input("Type your numbers: "))
        num_set.append(numbers_given)
    except ValueError:
        highest_num =  max(num_set)
        print("Invalid Input")
        print(f"Highest Number: {highest_num}")
        break