# Imagine a list - not very long, not very complicated, just a simple list containing some integer numbers.
# Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.
# Your task is to write a program which removes all the number repetitions from the list. The goal is to have a list in which all the numbers appear not more than once.
# Note: assume that the source list is hard-coded inside the code - you don't have to enter it from the keyboard. Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.
# Imagine a list - not very long, not very complicated, just a simple list containing some integer numbers. Some of these numbers may be repeated, and this is the clue. We don't want any repetitions. We want them to be removed.
# Your task is to write a program which removes all the number repetitions from the list. 
# The goal is to have a list in which all the numbers appear not more than once.
# Note: assume that the source list is hard-coded inside the code - you don't have to enter it from the keyboard. 
# Of course, you can improve the code and add a part that can carry out a conversation with the user and obtain all the data from her/him.

list = [1, 4, 4, 7, 6, 2, 9, 3, 8, 9]
list1 = []
for nr in list:
    if nr not in list1:     
        list1.append(nr)
print(list1)
