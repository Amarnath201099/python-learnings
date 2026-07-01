# Task 2: Flexible Calculator
# Objective: Create a calculator that supports dynamic operations.

print("Enter any on operator from add, multiply, factorial: ")
operator_type = input()

if operator_type not in ["add", "multiple", "factorial"]:
    print("Restart file and Enter valid operator type from given operators")
    exit()

def get_numbers():
    raw = input("Enter numbers separated by space: ").strip()
    
    if not raw:
        print("No numbers entered")
        return None 
    
    try:
        return list(map(int, raw.split()))
    except ValueError:
        print("Please enetr only numbers")
        return None
    

# used lambad function and also built-in sum function, if args are empty it returns zero
addition = lambda *args: sum(args) if args else 0

def multiplication(*args):
    product = 1
    for i in args:
        product *= i
    return product

def factorial(n):
    if(n == 0 or n == 1):
        return 1
    return n  * factorial(n - 1)


if(operator_type == "add"):
    nums = get_numbers()
    if nums is None:
        exit()
    result = addition(*nums)
    print("Addition of nums:",", ".join(str(i) for i in nums),": ", result)
elif(operator_type == "multiply"):
    nums = get_numbers()
    if nums is None:
        exit()
    result = multiplication(*nums)
    print("Multiplication of ", " ,".join(str(i) for i in nums),": ", result)
elif(operator_type == "factorial"):
    nums = get_numbers()
    if len(nums) != 1:
        print("Factorial requires exactly one number")
        exit()
    result = factorial(nums[0])
    print("Factorial of ",nums[0], ": ", result)





# 1. *args (Variable Arguments - How it works internally)
# - When we pass values using *nums, Python "unpacks" the list:
#     nums = [1, 2, 3]
#     function(*nums)  → becomes function(1, 2, 3)
#
# - Inside the function, *args collects these values as a TUPLE:
#     args = (1, 2, 3)
#
# - Difference:
#     function(nums)   → args = ([1,2,3])   (single list inside tuple)
#     function(*nums)  → args = (1,2,3)     (individual values)
#
# - This is why *args is required for dynamic arithmetic operations

# 2. Lambda Function (Execution model)
# - Lambda creates an anonymous function object at runtime
# - It is stored like a normal function reference:
#     addition = lambda *args: sum(args)
#
# - When called:
#     addition(1,2,3) → args = (1,2,3) → sum(tuple) is executed
#
# - Limitation:
#     Lambda can only contain ONE expression (no loops or multiple statements)

# 3. exit() (Program control flow)
# - exit() immediately stops Python execution
# - Internally raises a SystemExit exception
# - This prevents remaining code from running when invalid input is detected
# - Useful for early termination in CLI programs


# def addition(nums):
#     sum = 0
#     for i in nums:
#         sum += i
#     return sum 

# def multiplication(nums):
#     product = 1
#     for i in nums:
#         product *= i
#     return product

# def factorial(n):
#     if(n == 0 or n == 1):
#         return 1
#     return n  * factorial(n - 1)