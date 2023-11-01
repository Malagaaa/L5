# Write a program that reflects these changes and lets you practice with the concept of lists. Your task is to:

#	step 1: create an empty list named beatles;
#	step 2: use the append() method to add the following members of the band to the list: John Lennon, Paul McCartney, and George Harrison;
#	step 3: use the for loop and the append() method to prompt the user to add the following members of the band to the list: Stu Sutcliffe, and Pete Best;
#	step 4: use the del instruction to remove Stu Sutcliffe and Pete Best from the list;
#	step 5: use the insert() method to add Ringo Starr to the beginning of the list.

# Step 1
beatles = []
print("Step 1:", beatles)

# Step 2
beatles.append("John Lennon")
beatles.append("Paul McCartney")
beatles.append("George Harrison")
print("Step 2:", beatles)

# Step 3
for _ in range(2):
    member = input("Enter a band member's name: ")
    beatles.append(member)
print("Step 3:", beatles)

# Step 4
del beatles[3:5]
print("Step 4:", beatles)

# Step 5
beatles.insert(0, "Ringo Starr")
print("Step 5:", beatles)

# testing list length
print("The Fab", len(beatles))
