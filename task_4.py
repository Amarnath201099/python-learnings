# Task 4: Text File Analyzer
# Objective: Analyze a text file efficiently.

import time

file_name = input("Enter the file name: ")

if not file_name:
    print("Enter valid file name")
    exit()

if not file_name.endswith(".txt"):
    file_name += ".txt"



def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.perf_counter() # using time.pref_counter() has higher resolution and is designed for measuring elapsed time insted of time.time() with returns current wall-clock time
        result = func(*args, **kwargs)
        print("Execution Time:", time.perf_counter() - start_time)
        return result
    return wrapper


def read_lines(file):
    for line in file:
        yield line.strip()

@timer
def read_file(file_name):
    count_of_words = 0
    count_of_lines = 0

    with open(file_name, "r") as file:
        for line in read_lines(file):
            words = [word for word in line.split()]
            count_of_words += len(words)
            count_of_lines += 1
        return count_of_words, count_of_lines # returning the values as tuple

try:
    count_of_words, count_of_lines = read_file(file_name) # tuple uppacking
    print("Count of words: ", count_of_words )
    print("Count of lines: ", count_of_lines)
except FileNotFoundError:
    print("File does't exist with: ", file_name)
finally:
    print("Analyzing the file completed")



# ======================================
# CONCEPTS USED IN THIS PROGRAM
# ======================================

# 1. Decorator (@timer)
# - A decorator wraps another function to add extra behavior without modifying
#   the original function.
# - @timer is equivalent to:
#       read_file = timer(read_file)
# - Here it measures and prints the execution time of read_file().

# 2. Generator (yield)
# - read_lines() is a generator function because it uses 'yield'.
# - Unlike 'return', 'yield' pauses the function and remembers its state.
# - Each iteration produces one line at a time, making file reading memory-efficient.
# - Using line.strip() removes leading/trailing whitespace before yielding the line.

# 3. List Comprehension
# - Creates a list using concise syntax.
# - Example:
#       words = [word for word in line.split()]
# - It iterates through every word returned by split() and builds a new list.

# 4. Tuple Return and Unpacking
# - read_file() returns two values:
#       return count_of_words, count_of_lines
# - Python packs them into a tuple.
# - During assignment:
#       count_of_words, count_of_lines = read_file(file_name)
#   Python automatically unpacks the tuple into two variables.

# 5. Context Manager (with open)
# - 'with open(...)' automatically closes the file after use,
#   even if an exception occurs.
# - It is safer than manually calling file.close().

# 6. Exception Handling
# - try-except prevents the program from crashing if the file is not found.
# - finally always executes, regardless of whether an exception occurred.