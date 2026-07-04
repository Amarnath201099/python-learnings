# Task 12: Optimized User Profile System
# Objective: Build a production-ready, optimized user profile system using modern Python
# features.


from dataclasses import dataclass

from functools import lru_cache

import time

import asyncio

@dataclass
class UserProfile:

    __slots__ = ("id", "name", "age" , "role")
    
    id: int
    name: str
    age: int
    role: str

    def __post_init__(self):
        assert self.age > 0, "Age must be greater than zero"
        assert self.id > 0, "ID must be positive"
        assert self.name.strip(), "Name cannot be empty"
        assert self.role.strip(), "Role cannot be empty"
    
    def check_role(self) -> str:
        match self.role.lower():
            case "employee" | "admin" | "manager":
                return f"User is a {self.role}"
            
            case _:
                return "User does not belong to any category"

    def __str__(self):
        return f"id: {self.id} \n name: {self.name} \n age: {self.age} \n role: {self.role}"


@dataclass(frozen=True)
class UserSettings:
    theme: str = "dark"


@lru_cache(maxsize=100)
def load_profile(id, name, age, role) -> UserProfile:
    print(f"\nLoading profile from database")
    time.sleep(3)
    user = UserProfile(id, name, age, role)
    return user
    


users = [(1, "Jack", 34, "admin"), (1, "Jack", 34, "admin"), (2, "Alice", 30, "Manager"), (3, "Mark", 24, "employee")  ]

for user_data in users:
    user_obj = load_profile(*user_data)
    print(f"\n{user_obj}")
    print(user_obj.check_role())


class UserDatabaseConnection:

    async def __aenter__(self):
        await asyncio.sleep(3)
        print(f"\nConnecting to user database")
        return self

    async def __aexit__(self, exc_type, exc, tb):
        await asyncio.sleep(4)
        print("Disconnecting from user database")



async def main():

    async with UserDatabaseConnection() as db:
        print("Processing user databse")


asyncio.run(main())


# settings = UserSettings()

# settings.theme = "light"
        


# ==========================================================
# TASK 12 - REVISION NOTES (Optimized User Profile System)
# ==========================================================

# -------------------------------
# 1. @dataclass
# -------------------------------
# - Automatically generates __init__(), __repr__(), __eq__(), etc.
# - Reduces boilerplate code.
# - Best used for classes that mainly store data.

# -------------------------------
# 2. Type Hints
# -------------------------------
# - Improves readability and IDE support.
# - Used for static analysis (not runtime validation).
# - Example:
#     id: int
#     def check_role() -> str

# -------------------------------
# 3. __post_init__()
# -------------------------------
# - Runs automatically after dataclass __init__().
# - Best place for validation.
# - Better than manually calling validation methods.

# -------------------------------
# 4. Assertions
# -------------------------------
# - Used for internal assumptions during development.
# - Not for validating user input.
# - Always provide a meaningful error message.
#
# Example:
# assert age > 0, "Age must be positive"

# -------------------------------
# 5. __slots__
# -------------------------------
# - Restricts allowed instance attributes.
# - Prevents accidental attribute creation.
# - Saves memory for large numbers of objects.
# - Can slightly improve attribute access speed.
#
# Example:
# __slots__ = ("id", "name", "age", "role")
#
# Modern Alternative (Python 3.10+):
# @dataclass(slots=True)
#
# Difference:
# Manual __slots__:
# - Better for learning how slots work.
# - Must update manually when adding new attributes.
#
# dataclass(slots=True):
# - Automatically creates __slots__.
# - Cleaner and recommended in modern Python.

# -------------------------------
# 6. Frozen Dataclass
# -------------------------------
# - Makes objects immutable after creation.
# - Useful for configurations/settings.
#
# Example:
# @dataclass(frozen=True)

# -------------------------------
# 7. Pattern Matching (match-case)
# -------------------------------
# - Cleaner replacement for long if-elif chains.
# - Can combine multiple cases using |.
#
# Example:
# case "admin" | "employee":

# -------------------------------
# 8. f-Strings
# -------------------------------
# - Preferred way to format strings.
# - Faster and more readable than concatenation.
#
# Example:
# f"Welcome {name}"

# -------------------------------
# 9. @lru_cache
# -------------------------------
# - Caches function results.
# - Avoids repeating expensive operations.
# - Function executes only once for identical arguments.
#
# Best for:
# - Database lookups
# - API requests
# - Expensive calculations
#
# Note:
# Cached functions should ideally be pure
# (same input -> same output).

# -------------------------------
# 10. Async Context Manager
# -------------------------------
# - Uses:
#     async with
# - Methods:
#     __aenter__()
#     __aexit__()
# - Automatically acquires and releases resources.
#
# Examples:
# - Database connections
# - HTTP sessions
# - Network resources

# IMPORTANT:
# Inside async code:
# ✔ await asyncio.sleep()
# ✘ time.sleep()   (blocks event loop)

# -------------------------------
# 11. Security Best Practices
# -------------------------------
# - Avoid eval().
# - Never build SQL queries using string concatenation.
# - Use parameterized queries.
# - Validate user input.
# - Never expose secrets in code.

# -------------------------------
# 12. My Learning Notes / Doubts
# -------------------------------
# ✔ __post_init__ is called automatically after object creation.
#
# ✔ Assertions are for developer assumptions,
#   NOT user input validation.
#
# ✔ lru_cache stores function results based on arguments.
#   Same arguments -> cached result returned.
#
# ✔ Async functions must avoid blocking calls like time.sleep().
#
# ✔ Manual __slots__ helped understand memory optimization.
#   Modern Python usually prefers @dataclass(slots=True).
#
# ✔ Frozen dataclasses are useful for immutable configuration
#   objects (settings, preferences, constants).

# -------------------------------
# 13. Final Flow
# -------------------------------
# Create UserProfile
#        ↓
# __post_init__ validates data
#        ↓
# load_profile() checks cache
#        ↓
# If cached → return immediately
# Else → simulate database lookup
#        ↓
# Return UserProfile object
#        ↓
# async with manages database connection
#        ↓
# Automatically disconnects on exit

# ==========================================================