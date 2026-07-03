# Task 9: Log File Analyzer
# Objective: Extract errors and warnings from logs using regex and functional tools.

import re 

from functools import reduce

pattern = r"^(ERROR|WARNING):\s*(.*)$"

log_file = "log_details.log"



with open(log_file, "r") as file:
    logs = file.readlines()
    filtered_logs = list(filter(lambda line: re.search(pattern, line), logs))


structured_logs = list(map(lambda line: {"Level": re.search(pattern, line).group(1), "Message": re.search(pattern, line).group(2)}, filtered_logs))

print("Extracted logs: ")

for log in structured_logs:
    print(log)

total_errors = reduce(lambda count, log: count + (1 if log["Level"] == "ERROR" else 0), structured_logs, 0 )

print("Total Errors: ", total_errors)

total_warnings = reduce(lambda count, log: count + (1 if log["Level"] == "WARNING" else 0), structured_logs, 0)

print("Total Warnings", total_warnings)


total_matches = reduce(lambda count, log: count + 1, structured_logs, 0)

print("Total Matches: ", total_matches)










# ============================================================
# QUICK REVISION NOTES - REGEX, FILTER, MAP, REDUCE & LAMBDA
# ============================================================

# ----------------------------
# 1. filter()
# ----------------------------
# Syntax:
# filter(function, iterable)
#
# Purpose:
# Keeps only the items for which the function returns True (or a truthy value).
#
# Without lambda:
# def is_valid(item):
#     return condition
# filter(is_valid, iterable)
#
# With lambda:
# filter(lambda item: condition, iterable)
#
# Think:
# "Should I KEEP this item?"
#
# Example:
# filter(lambda x: x % 2 == 0, [1,2,3,4])
# -> keeps only even numbers.


# ----------------------------
# 2. map()
# ----------------------------
# Syntax:
# map(function, iterable)
#
# Purpose:
# Applies a function to every item and returns transformed values.
#
# Without lambda:
# def square(x):
#     return x*x
# map(square, numbers)
#
# With lambda:
# map(lambda x: x*x, numbers)
#
# Think:
# "What should this item BECOME?"
#
# Example:
# map(lambda x: x*x, [1,2,3])
# -> [1,4,9]


# ----------------------------
# 3. reduce()
# ----------------------------
# Syntax:
# reduce(function, iterable, initial_value)
#
# Purpose:
# Combines all values into a single result.
#
# Function always accepts TWO arguments:
# (accumulator, current_item)
#
# Without lambda:
# def add(total, num):
#     return total + num
#
# reduce(add, numbers, 0)
#
# With lambda:
# reduce(lambda total, num: total + num, numbers, 0)
#
# Think:
# "Combine what I've built so far with the current item."


# ----------------------------
# 4. Lambda Function
# ----------------------------
# Lambda is just an anonymous (unnamed) function.
#
# Normal function:
#
# def square(x):
#     return x*x
#
# Lambda:
#
# lambda x: x*x
#
# They are functionally the same.
#
# Lambda is commonly used when the function is small and used only once.


# ----------------------------
# 5. Difference between filter, map & reduce
# ----------------------------
#
# filter() -> Removes unwanted items.
#
# map() -> Changes every item.
#
# reduce() -> Produces one final value.
#
# Easy way to remember:
#
# filter -> KEEP?
# map    -> CHANGE?
# reduce -> COMBINE?


# ----------------------------
# 6. Why list() is used?
# ----------------------------
# In Python,
#
# filter() returns a FILTER OBJECT (iterator)
# map() returns a MAP OBJECT (iterator)
#
# Unlike JavaScript, they DO NOT return a list.
#
# To see all values:
#
# list(filter(...))
# list(map(...))
#
# OR iterate using:
#
# for item in filter(...):
#     ...
#
# Iterators are LAZY:
# They calculate values only when needed.


# ----------------------------
# 7. Iterator Important Note
# ----------------------------
# Iterators can usually be consumed only ONCE.
#
# Example:
#
# nums = map(lambda x: x*x, [1,2,3])
#
# list(nums)
# -> [1,4,9]
#
# list(nums)
# -> []
#
# After being exhausted, an iterator has no more values.


# ----------------------------
# 8. Regex Pattern Used
# ----------------------------
#
# pattern = r"^(ERROR|WARNING):\s*(.*)$"
#
# Breakdown:
#
# ^               -> Start of line
#
# (ERROR|WARNING)
#                 -> Match ERROR or WARNING
#                 -> Capturing Group 1
#
# :               -> Literal colon
#
# \s              -> One whitespace character
#
# *               -> Zero or more of previous character
#
# \s*             -> Zero or more spaces
#
# (.*)            -> Capture everything after colon
#                 -> Capturing Group 2
#
# $               -> End of line


# ----------------------------
# 9. Regex Groups
# ----------------------------
#
# Parentheses () create CAPTURING GROUPS.
#
# Example:
#
# pattern = r"(ERROR|WARNING):\s*(.*)"
#
# ERROR: File missing
#
# group(1) -> ERROR
# group(2) -> File missing
#
# Group numbering starts at 1.
#
# group(3), group(4), etc. exist only if the regex
# contains that many capturing groups.
#
# Example:
#
# (\d+)-(\d+)-(\d+)
#
# group(1) -> Year
# group(2) -> Month
# group(3) -> Day


# ----------------------------
# 10. Regex Quantifiers
# ----------------------------
#
# *      -> 0 or more
#
# +      -> 1 or more
#
# ?      -> 0 or 1
#
# {n}    -> Exactly n times
#
# {m,n}  -> Between m and n times
#
# Examples:
#
# \s*    -> "", " ", "     "
#
# \s+    -> " ", "    " (at least one space)
#
# \d{3}  -> 123
#
# a{2,4} -> aa, aaa, aaaa


# ----------------------------
# 11. Truthy & Falsy in filter()
# ----------------------------
#
# filter() does NOT require True/False explicitly.
#
# Any truthy value keeps the item.
#
# Example:
#
# re.search(...) returns:
#
# Match Object -> Truthy (keep)
#
# None -> Falsy (discard)
#
# That's why this works:
#
# filter(lambda line: re.search(pattern, line), logs)


# ----------------------------
# 12. What Python Internally Does
# ----------------------------
#
# filter(func, items)
#
# ≈
#
# result = []
#
# for item in items:
#     if func(item):
#         result.append(item)
#
#
# map(func, items)
#
# ≈
#
# result = []
#
# for item in items:
#     result.append(func(item))
#
#
# reduce(func, items, initial)
#
# ≈
#
# accumulator = initial
#
# for item in items:
#     accumulator = func(accumulator, item)
#
# return accumulator


# ============================================================
# MEMORY TRICK
# ============================================================
#
# filter -> KEEP?
#
# map    -> CHANGE?
#
# reduce -> COMBINE?
#
# lambda -> Short anonymous function.
#
# ()     -> Capturing Groups in regex.
#
# group(n) -> nth captured value.
#
# map/filter return ITERATORS in Python.
#
# Use list() to materialize them or loop over them.
#
# Iterators are lazy and are exhausted after use.
#
# ============================================================