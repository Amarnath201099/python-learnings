# Task 5: Mutability & Scope Demo
# Objective: Demonstrate mutability and scope behavior.

input_list = input("Enter list with space separated: ").split()

if not input_list:
    print("List can not be empty")
    exit()

input_tuple = tuple(input_list)



# checking mutability in list

input_list[0] = "change"
print("Modified List", input_list)


#checking mutability in tuple

try:
    input_tuple[0] = "change"
except TypeError:
    print("Tuple can't be modified")


#checking slice on list and tuple

print("Sliced List: ", input_list[1:])

print("Sliced Tuple: ", input_tuple[1:])

count_a = 0
count_b = 0

def update():
    try:
        global count_a
        count_a +=1
        count_b += 3
    except:
        print("count_b can't be changed as its not refered with global keyword to modify it locally") 

update()

print("Count A", count_a)
print("Count_B", count_b)


