#Let's assume that you've chosen the following numbers in the lottery: 3, 7, 11, 42, 34, 49. The numbers that have been drawn are: 5, 11, 9, 42, 3, 49.
#The question is: how many numbers have you hit?

your_numbers = [3, 7, 11, 42, 34, 49]
drawn_numbers = [5, 11, 9, 42, 3, 49]

# Use set intersection to find the matching numbers
matching_numbers = set(your_numbers) & set(drawn_numbers)

# Calculate the count of matching numbers
matching_count = len(matching_numbers)

print("You have hit", matching_count, "numbers in the lottery.")
