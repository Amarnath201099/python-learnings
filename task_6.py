# Task 6: Mini Banking System
# Objective: Build a basic banking system using OOP.

class Account:
    def __init__(self,name, account_number, balance = 0):
        self.name = name
        self.account_number = account_number
        self.__balance = balance
    
    def deposit(self, amount):
        if(amount <= 0):
            return "Invalid Deposit"
        self.__balance += amount
        return self.__balance

    def withdraw(self, amount):
        if(amount <= 0):
            return "Invalid Withdrawal"
        if(amount > self.__balance):
            return "Insufficient Balance"
        
        self.__balance -= amount
        return self.__balance
    
    def get_balance(self):
        return self.__balance
    
    def __str__(self):
        return(
            f"Account Holder: {self.name}\n"
            f"Account Number: {self.account_number}\n"
            f"Balance:  {self.get_balance():.2f}"
        )


class SavingsAccount(Account):
    def __init__(self, name, account_number, balance = 0, interest_rate = 0.05):
        super().__init__(name, account_number, balance)
        self.interest_rate = interest_rate

    def add_interest(self):
        interest = self.get_balance() * self.interest_rate
        return self.deposit(interest)
        
    

user = SavingsAccount("User_1", "1234", 1000)

print(user)

deposit_amount = int(input("Enter deposit amount:"))

print(user.deposit(deposit_amount))

withdraw_amount = int(input("Enter withdrow amount:"))

print(user.withdraw(withdraw_amount))

print(user.get_balance())

print(user.add_interest())


# =========================================================
# PYTHON OOP CONCEPTS USED (REVISION NOTES)
# =========================================================

# 1. CLASS & OBJECT
# - Class is a blueprint (Account, SavingsAccount)
# - Object is an instance of a class
#   Example: user = SavingsAccount(...)

# =========================================================

# 2. __init__ (CONSTRUCTOR)
# - Automatically runs when an object is created
# - Used to initialize variables
#   Example:
#   def __init__(self, name, account_number, balance=0)

# =========================================================

# 3. self KEYWORD
# - Refers to the current object instance
# - Used to access variables and methods inside the class
#   Example: self.name, self.__balance

# =========================================================

# 4. ENCAPSULATION (__balance)
# - __balance is a private variable (name mangling)
# - Cannot be accessed directly outside the class
# - Must use methods like get_balance(), deposit(), withdraw()

# =========================================================

# 5. INHERITANCE (SavingsAccount → Account)
# - Child class inherits properties and methods of parent class
# - Saves code duplication
# - Example: SavingsAccount automatically gets deposit/withdraw

# =========================================================

# 6. super()
# - Used to call parent class constructor/methods
# - Ensures parent class is properly initialized
#   Example:
#   super().__init__(name, account_number, balance)

# =========================================================

# 7. METHOD OVERLOADING (SIMULATED)
# - Python does NOT support true overloading
# - We simulate behavior using default arguments or logic checks
#   Example: deposit(amount)

# =========================================================

# 8. __str__ (STRING REPRESENTATION)
# - Controls what gets printed when we do print(object)
# - Without it, Python prints memory address
# - Example:
#   def __str__(self):
#       return formatted string

# =========================================================

# 9. METHODS (BEHAVIOR FUNCTIONS)
# - deposit(), withdraw(), get_balance(), add_interest()
# - Define actions an object can perform
# - Operate on object data (state)

# =========================================================

# 10. BUSINESS LOGIC FLOW
# - Object created → user
# - Deposit → increases balance
# - Withdraw → decreases balance (with checks)
# - Interest → calculated using balance * rate

# =========================================================

# 11. KEY OOP IDEA
# - Data (balance) + Behavior (methods) bundled together
# - This is called ENCAPSULATION IN PRACTICE

# =========================================================