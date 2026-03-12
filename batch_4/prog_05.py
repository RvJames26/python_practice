#Create a program that ask user to input a number, continue asking until the user input is invalid. Display the average.
nums = []
nums_ask = 0
nums_ask += 1
num_start = 0
while True:
    try:
        for i in range(nums_ask):
            given_nums = float(input("Input numbers: "))
            num_start += i
    except ValueError:
        print("Invalid Input")
        print(num_start / nums_ask)