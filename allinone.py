# Python Basics: A Beginner-Friendly Example File

# -----------------------------
# 1. Variables and Data Types
# -----------------------------
name = "Alice"            # String
age = 25                  # Integer
height = 5.4              # Float
is_student = True         # Boolean

print("Name:", name)
print("Age:", age)
print("Height:", height)
print("Student:", is_student)

# -----------------------------
# 2. Lists and Indexing
# -----------------------------
favorite_fruits = ["apple", "banana", "mango"]
print("First fruit:", favorite_fruits[0])  # Indexing starts at 0

# Add a fruit to the list
favorite_fruits.append("orange")
print("All fruits:", favorite_fruits)

# -----------------------------
# 3. Conditions and If-Else
# -----------------------------
if age >= 18:
    print("You are an adult.")
else:
    print("You are a minor.")

# -----------------------------
# 4. Loops: For and While
# -----------------------------
print("\nFor loop:")
for fruit in favorite_fruits:
    print(fruit)

print("\nWhile loop:")
count = 0
while count < 3:
    print("Counting:", count)
    count += 1

# -----------------------------
# 5. Functions
# -----------------------------
def greet_user(name):
    return f"Hello, {name}!"

message = greet_user("Bob")
print(message)

# -----------------------------
# 6. Dictionaries
# -----------------------------
student = {
    "name": "Charlie",
    "age": 20,
    "grades": [90, 85, 88]
}
print("Student Name:", student["name"])
print("Student Grades:", student["grades"])

# -----------------------------
# 7. Classes and Objects
# -----------------------------
class Dog:
    def __init__(self, name, breed):
        self.name = name
        self.breed = breed

    def bark(self):
        print(f"{self.name} says woof!")

my_dog = Dog("Buddy", "Golden Retriever")
my_dog.bark()

# -----------------------------
# 8. File Handling (Reading & Writing)
# -----------------------------
with open("sample.txt", "w") as file:
    file.write("This is a sample file.\nSecond line.")

with open("sample.txt", "r") as file:
    content = file.read()
    print("\nFile Content:\n", content)

# -----------------------------
# 9. Exception Handling
# -----------------------------
try:
    result = 10 / 0
except ZeroDivisionError:
    print("You can't divide by zero!")

# -----------------------------
# 10. Importing Modules
# -----------------------------
import math
print("Square root of 16 is:", math.sqrt(16))
