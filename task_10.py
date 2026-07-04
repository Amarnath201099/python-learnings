import pandas as pd
import asyncio

csv_files = ["students1.csv", "students2.csv", "students3.csv"]


def process_file(file_name):
    df = pd.read_csv(file_name)
    # print(f"\nProcessing {file_name}")
    # print(df)
    df["Marks"] = df["Marks"].fillna(0)
    df["Age"] = df["Age"].fillna(df["Age"].mean())
    df = df.dropna(subset=["Name"])
    return df 


async def process_csv_files():
    tasks = [asyncio.to_thread(process_file, file) for file in csv_files]
    results = await asyncio.gather(*tasks)
    
    for i, df in enumerate(results, start=1):
        print(f"\nStudents of Class {i}:")
        print(df)
        print(f"Count of Students in Class {i}: ", df["Name"].count())
        print(f"Average Age of Class {i}: ", df["Age"].mean())
        print(f"Max Marks in Class {i}: ", df["Marks"].max())

        print(f"Students till row {i}: \n", df.loc[:i, ["Name", "Marks"]])
        print(f"Studnet {i}: \n", df.iloc[i])

        output = f"Student{i}.xlsx"
        df.to_excel(output, index=False)


asyncio.run(process_csv_files())




# ==========================================================
# QUICK REVISION NOTES
# ==========================================================

# 1. asyncio.to_thread()
#    - Used to run a normal (blocking) function in a separate thread.
#    - Required because pandas.read_csv() is synchronous/blocking.
#    - Prevents the event loop from being blocked.
#
#    Syntax:
#    await asyncio.to_thread(function, arg1, arg2)

# ----------------------------------------------------------

# 2. asyncio.gather()
#    - Runs multiple coroutines concurrently.
#    - Waits until all tasks complete.
#    - Returns results in the same order as the tasks.

# ----------------------------------------------------------

# 3. Why use *tasks ?
#    - '*' is the unpacking operator.
#    - Converts a list into separate arguments.
#
#    Example:
#    tasks = [task1, task2, task3]
#    asyncio.gather(*tasks)
#
#    is equivalent to:
#    asyncio.gather(task1, task2, task3)

# ----------------------------------------------------------

# 4. Missing Value Handling
#
#    fillna(value)
#       -> Replace missing values.
#
#    dropna()
#       -> Remove rows with missing values.
#
#    dropna(subset=["column"])
#       -> Remove rows only if specified column has missing value.

# ----------------------------------------------------------

# 5. Common Data Cleaning
#
#    df["Marks"] = df["Marks"].fillna(0)
#    df["Age"] = df["Age"].fillna(df["Age"].mean())
#    df = df.dropna(subset=["Name"])

# ----------------------------------------------------------

# 6. loc vs iloc
#
#    loc[]
#      - Label-based indexing.
#      - Uses row/column labels.
#
#    iloc[]
#      - Position-based indexing.
#      - Uses integer positions (0,1,2,...)

# Examples:
#
# df.loc[:, ["Name", "Marks"]]
# df.iloc[:5]
# df.iloc[0]

# ----------------------------------------------------------

# 7. Useful Statistics
#
# df["Marks"].mean()      -> Average
# df["Marks"].sum()       -> Total
# df["Marks"].count()     -> Count
# df["Marks"].max()       -> Maximum
# df["Marks"].min()       -> Minimum
# df.describe()           -> Summary statistics

# ----------------------------------------------------------

# 8. Export Data
#
# df.to_excel("Student1.xlsx", index=False)
#
# index=False prevents writing DataFrame index into Excel.

# ----------------------------------------------------------

# 9. String Formatting
#
# Preferred:
# output = f"Student{i}.xlsx"
#
# Instead of:
# "Student" + str(i) + ".xlsx"

# ----------------------------------------------------------


# 10. Flow of this Program
#
# Read CSV
#      ↓
# Clean missing values
#      ↓
# Process files concurrently using asyncio.to_thread()
#      ↓
# asyncio.gather() waits for all files
#      ↓
# Compute statistics
#      ↓
# Select required rows/columns
#      ↓
# Export cleaned DataFrame to Excel

# ==========================================================
# Interview / Viva Questions
# ==========================================================
#
# ✓ Why use asyncio?
#    -> To execute multiple independent tasks concurrently.
#
# ✓ Why use asyncio.to_thread()?
#    -> Because pandas.read_csv() is blocking.
#
# ✓ Why not make process_file() async?
#    -> read_csv() is synchronous, so async alone won't make it non-blocking.
#
# ✓ Why use * in gather()?
#    -> To unpack a list into separate coroutine arguments.
#
# ✓ Difference between loc and iloc?
#    -> loc = labels, iloc = integer positions.
#
# ✓ Difference between fillna() and dropna()?
#    -> fillna() replaces missing values.
#    -> dropna() removes rows/columns with missing values.
#
# ✓ Why use index=False in to_excel()?
#    -> Prevents DataFrame index from being written to the Excel file.
#
# ==========================================================




# ============================
# IMPORTANT NOTES
# ============================

# DataFrame -> Table (rows & columns)
# Series -> Single column

# head() -> First 5 rows
# tail() -> Last 5 rows
# If the DataFrame has <=5 rows, df, head(), and tail() look the same.

# shape -> (rows, columns)
# columns -> Column names
# info() -> Data types & missing values
# describe() -> Statistics for numeric columns

# df["Name"] -> Series
# df[["Name"]] -> DataFrame

# iloc -> Integer index
# loc -> Row labels & column names

# isnull() -> Find missing values
# isnull().sum() -> Count missing values

# dropna() -> Remove rows with missing values
# fillna() -> Fill missing values

# IMPORTANT:
# fillna() does NOT change the DataFrame unless assigned.
#
# Correct:
# df["Age"] = df["Age"].fillna(df["Age"].mean())

# mean() -> Average
# max() -> Highest value
# min() -> Lowest value
# sum() -> Total
# count() -> Non-null values

# Filtering
# &
# |
#
# Example:
# df[(df["Age"] > 20) & (df["Marks"] > 80)]

# Saving
# df.to_csv("new.csv", index=False)
# df.to_excel("students.xlsx", index=False)

# NOTE:
# Pandas only changes the DataFrame in memory.
# The original CSV is NOT modified unless you save it.




# ----------------------------------------------------
# # Missing Values
# # ----------------------------------------------------

# # Check missing values (True = missing, False = not missing)
# print(df.isnull())

# # Count missing values in each column
# print(df.isnull().sum())

# # Remove rows containing missing values
# # (Returns a new DataFrame)
# # print(df.dropna())

# # Replace all missing values with 0
# # (Returns a new DataFrame)
# print(df.fillna(0))

# # Replace missing Age values with the average age
# # (Returns a new Series)
# print(df["Age"].fillna(df["Age"].mean()))

# # Original DataFrame (still unchanged)
# print(df)


# # ----------------------------------------------------
# # Basic Statistics
# # ----------------------------------------------------

# # Average Marks
# print("Average marks:", df["Marks"].mean())

# # Highest Marks
# print("Highest marks:", df["Marks"].max())

# # Lowest Marks
# print("Lowest marks:", df["Marks"].min())

# # Number of non-null values
# print("Count:", df["Marks"].count())

# # Sum of all marks
# print("Total:", df["Marks"].sum())


# # ----------------------------------------------------
# # Saving Files
# # ----------------------------------------------------

# # Save DataFrame as CSV
# print("CSV:", df.to_csv("new.csv", index=False))

# # Save DataFrame as Excel
# print("Excel:", df.to_excel("students.xlsx", index=False))


# # Read the CSV file and store it in a DataFrame
# df = pd.read_csv("students.csv")

# # ----------------------------------------------------
# # Basic Information
# # ----------------------------------------------------

# # Returns the type of object
# # Output: <class 'pandas.core.frame.DataFrame'>
# print(type(df))

# # Prints the complete DataFrame
# # If the dataset is small, all rows are displayed.
# # If the dataset is large, pandas displays only some rows.
# print(df)

# # Displays the first 5 rows by default
# # You can also use df.head(3) to display the first 3 rows.
# print("head:")
# print(df.head())

# # Displays the last 5 rows by default
# # You can also use df.tail(2) to display the last 2 rows.
# print("tail:")
# print(df.tail())

# # Prints all column names
# print("columns:")
# print(df.columns)

# # Returns (number_of_rows, number_of_columns)
# print("shape")
# print(df.shape)

# # Displays information about the DataFrame:
# # - Number of rows
# # - Column names
# # - Data types
# # - Non-null values
# print("info")
# print(df.info())

# # Gives statistical summary for numeric columns:
# # count, mean, std, min, max, etc.
# print("describe")
# print(df.describe())

# # ----------------------------------------------------
# # Selecting Columns
# # ----------------------------------------------------

# # Select a single column
# # Result type: Series
# print("single column:", df["Name"])

# # Select multiple columns
# # Result type: DataFrame
# print("multiple columns:", df[["Name", "Marks"]])

# # ----------------------------------------------------
# # Selecting Rows
# # ----------------------------------------------------

# # iloc = Integer Location (uses index positions)

# # First row (index position 0)
# print("first row", df.iloc[0])

# # Second row
# print("second row", df.iloc[1])

# # Row 0, Column 2
# print("specific value:", df.iloc[0, 2])

# # ----------------------------------------------------
# # loc
# # ----------------------------------------------------

# # loc = Label Location
# # Uses row labels and column names

# # First row using label
# print("using loc:", df.loc[0])

# # All rows with only Name and Age columns
# print("using loc:", df.loc[:, ["Name", "Age"]])

# # ----------------------------------------------------
# # Filtering Data
# # ----------------------------------------------------

# # Students whose Marks are greater than 80
# print("Students above 80 marks")
# print(df[df["Marks"] > 80])

# # Students whose Age is greater than 20
# print("Students age greater than 20")
# print(df[df["Age"] > 20])

# # Multiple conditions
# # Age > 20 AND Marks > 80
# print("Two conditions")
# print(df[(df["Age"] > 20) & (df["Marks"] > 80)])


# # ====================================================
# # IMPORTANT NOTES (Revision)
# # ====================================================

# # 1. DataFrame
# #    A DataFrame is a table with rows and columns.

# # 2. Series
# #    A single column in a DataFrame is called a Series.

# # 3. head()
# #    Shows the first 5 rows by default.
# #    Syntax:
# #       df.head()
# #       df.head(10)

# # 4. tail()
# #    Shows the last 5 rows by default.
# #    Syntax:
# #       df.tail()
# #       df.tail(3)

# # 5. Why are df, head(), and tail() showing the same output?
# #
# #    Because your CSV file probably contains 5 or fewer rows.
# #
# #    Example:
# #
# #    CSV contains only 5 rows
# #
# #    df
# #    -----
# #    row1
# #    row2
# #    row3
# #    row4
# #    row5
# #
# #    df.head()  --> first 5 rows = all rows
# #    df.tail()  --> last 5 rows = all rows
# #
# #    Therefore all three outputs are identical.
# #
# #    If your CSV had 100 rows:
# #
# #    df.head() -> rows 1 to 5
# #    df.tail() -> rows 96 to 100
# #    df        -> all 100 rows (or a truncated display)

# # 6. iloc
# #    Uses integer positions.
# #
# #    Examples:
# #       df.iloc[0]
# #       df.iloc[2]
# #       df.iloc[0, 1]

# # 7. loc
# #    Uses row labels and column names.
# #
# #    Examples:
# #       df.loc[0]
# #       df.loc[:, ["Name", "Marks"]]

# # 8. Shape
# #    Returns:
# #       (rows, columns)

# # 9. Columns
# #    Returns all column names.

# # 10. info()
# #     Useful for checking:
# #     - Missing values
# #     - Data types
# #     - Memory usage

# # 11. describe()
# #     Works mainly on numeric columns.
# #     Gives:
# #     - count
# #     - mean
# #     - std
# #     - min
# #     - max
# #     - quartiles

# # 12. Filtering
# #
# #     Single condition:
# #     df[df["Marks"] > 80]
# #
# #     Multiple conditions:
# #     &
# #     |
# #
# #     Examples:
# #
# #     df[(df["Age"] > 20) & (df["Marks"] > 80)]
# #
# #     df[(df["Age"] > 20) | (df["Marks"] > 80)]

# # 13. Single vs Multiple Columns
# #
# #     df["Name"]          -> Series
# #
# #     df[["Name"]]        -> DataFrame
# #
# #     df[["Name","Age"]]  -> DataFrame

# # 14. Most commonly used DataFrame methods
# #
# #     df.head()
# #     df.tail()
# #     df.info()
# #     df.describe()
# #     df.shape
# #     df.columns
# #     df.dtypes
# #     df.isnull()
# #     df.drop()
# #     df.rename()
# #     df.sort_values()
# #     df.groupby()

# # 15. Interview Tip
# #
# #     loc  -> Label based indexing
# #     iloc -> Integer position based indexing