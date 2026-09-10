# Create list of lists: last_semester_gradebook
last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below: 
# Create lists: subjects, grades
subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97, 85, 88]
# Create list of lists: gradebook
gradebook = [["physics", 98], ["calculus", 97], ["poetry", 85], ["history", 88]]
# Print, append new items and re print
print(gradebook)
gradebook.append(["computer science", 100])
print(gradebook)
gradebook.append(["visual arts", 93])
print(gradebook[5])
# Add 5 to gradebook[5][1]
gradebook[5][1] += 5
# Print gradebook, gradebook[1]
print(gradebook)
print(gradebook[1])
# Remove 85, "Pass" from gradebook and print
gradebook[2].remove(85)
gradebook[2].append("Pass")
print(gradebook)
# Create variable: full gradebook and print
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)
