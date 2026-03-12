#Create a program that ask user to input a number, continue asking until the user input is invalid. 
# Display the number with the most number of duplicate.
num_set = []
while True:
    try:
        numbers_given = float(input("Type your numbers: "))
        num_set.append(numbers_given)
    except ValueError:
        most_duplicate_num =  max((num_set), key=num_set.count)
        print("Invalid Input")
        print(f"Most duplicate: {most_duplicate_num}")
        break