# Task 7: Resource Manager & Iterator
# Objective: Implement custom context manager and iterator.

file = "data.txt"

class FileReader:
    def __enter__(self):
        print("Opening the file")
        self.file = open(file, "r")
        return self.file
    

    def __exit__(self, exc_type, exc, tb):
        self.file.close()
        print("Reading completed")


class FileIterator:
    def __init__(self, file):
        self.file = file
        self.num = 0

    def __iter__(self):
        return self

    def __next__(self):
        while True:
            line = self.file.readline()

            if line == "":
                raise StopIteration
        
            if line.strip() == "":
                continue # skip blank lines        

            self.num += 1
            return f"{self.num}. {line.strip()}"

with FileReader() as file:
    print("In progress")
    for line in FileIterator(file):
        print(line)



"""
==================== QUICK REVISION NOTES ====================

1. Context Manager (__enter__ / __exit__)
------------------------------------------------
- __enter__ runs first when 'with' starts.
- It should OPEN and RETURN the resource (usually file object).
- 'as file' receives whatever __enter__ returns.
- __exit__ always runs at the end (even if error happens).
- It should CLOSE the resource.

Example flow:
with FileReader() as file:
    file = __enter__() return value

==============================================================

2. Difference: "" vs "\n"
------------------------------------------------
- ""   -> End of file (STOP iteration)
- "\n" -> Blank line inside file (valid line, not end)

==============================================================

3. Iterator (__iter__ and __next__)
------------------------------------------------
- __iter__ returns the iterator object itself.
- __next__ returns next value each time.

Why "return self"?
- It means: "this object is its own iterator"
- Required so Python can call __next__ repeatedly on same object
- Without it, for-loop won't know how to iterate

Flow:
for item in obj:
    calls iter(obj) -> __iter__()
    then repeatedly calls __next__()

==============================================================

4. StopIteration
------------------------------------------------
- MUST be raised when iteration ends
- Without it → infinite loop

Example:
if line == "":
    raise StopIteration

==============================================================

5. Skipping blank lines
------------------------------------------------
- line.strip() == "" means line is empty or whitespace
- Use 'continue' to skip it

==============================================================

6. Your final logic idea
------------------------------------------------
FileReader -> opens/closes file (resource manager)
FileIterator -> reads file line-by-line safely
Handles:
- EOF stop
- blank line skip
- line numbering

==============================================================
"""