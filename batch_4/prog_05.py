#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
nums = []
attempt = 0
while True:
    attempt += 1
    try:
        given_nums = float(input("Input numbers: "))
        nums.append(given_nums)
        total = sum(nums)
        average = total / attempt
    except ValueError:
        print("Invalid Input")
        print(f"Average: {average}")
        break