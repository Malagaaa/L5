# Considering the following snippet, how can you reverse a list of 100 elements? 
# hint: you have to use for loop, for another hint, ask the teacher, or the stackoverflow

# Create a sample list of 100 elements
my_list = list(range(1, 101))

# Using a for loop to reverse the list
list_length = len(my_list)
for i in range(list_length // 2):
    my_list[i], my_list[list_length - 1 - i] = my_list[list_length - 1 - i], my_list[i]

# Print the reversed list
print(my_list)
