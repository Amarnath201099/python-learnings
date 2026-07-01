# Student Data Management System
# Objective: Build a program to store and manage student academic data.

print("Student Name: ")
student_name = input()

print("Roll Number: ")
roll_number = input()

print("Enter list of subjest with space for each subject: ")
list_of_subjects = list(map(str.capitalize ,input().split(" ")))

unique_subs = set(list_of_subjects)


list_of_subjects = list(unique_subs)

marks_for_each_sub = {}

for  i in list_of_subjects:
    print("Marks of ",i ," :")
    marks_for_each_sub[i] = int(input())


print(student_name)
print(roll_number)
print(list_of_subjects)
print(marks_for_each_sub)


# list → keeps items in order and allows duplicates (same value can appear many times)
# set → removes duplicates but does NOT keep the original order (order may change)
# dict.fromkeys(list) → removes duplicates and keeps the same order as the original list
# use set when you only care about unique values, not order
# use dict.fromkeys when you want unique values but also want to keep the original sequence

# Why order is lost in set (simple idea):
# A set stores elements using a hash table.
# So Python places items based on their hash value, not their position in the list.
# That’s why:
# list → ordered (index-based storage)
# set → unordered (hash-based storage)