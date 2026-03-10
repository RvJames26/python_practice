#Create a program that ask user to input a number,
#  continue asking until the user input is invalid.
#  Display the number from lowest to highest. Clue: sort() function
num_set = []
while True:
    try:
        numbers_given = float(input("Type your numbers: "))
        num_set.append(numbers_given)
    except ValueError:
        num_set.sort()
        print("Invalid Input")
        print(f"Sorted list: {num_set}")
        break