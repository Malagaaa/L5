# There once was a hat. The hat contained no rabbit, but a list of five numbers: 1, 2, 3, 4, and 5.
# Your task is to:
# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (step 1)
# write a line of code that removes the last element from the list (step 2)
# write a line of code that prints the length of the existing list (step 3.)

# write a line of code that prompts the user to replace the middle number in the list with an integer number entered by the user (step 1)
user_input = int(input("Enter a number to replace the middle number in the list: "))
hat_list = [1, 2, 3, 4, 5]
hat_list[2] = user_input
print(hat_list)

# write a line of code that removes the last element from the list (step 2)
hat_list = [1, 2, 3, 4, 5]
hat_list.pop()
print(hat_list)

# write a line of code that prints the length of the existing list (step 3.)
print("The length of the list is:", len(hat_list))