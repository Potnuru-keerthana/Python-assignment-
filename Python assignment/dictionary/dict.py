# Create a dictionary with student ID as key and student name as value
students = {
    101: "Alice",
    102: "Bob",
    103: "Charlie",
    104: "David",
    105: "Eve"
}
print("Initial Dictionary:")
print(students)

# 1.1 Adding a new student to the dictionary
students[106] = "Frank"
print("\nDictionary after adding a new student:")
print(students)

# 1.2 Updating an existing student's name
students[103] = "Charlie Brown"  # Updating student with ID 103
print("\nDictionary after updating a student's name:")
print(students)

# 1.3 Accessing the name of the student with ID 102
student_name = students.get(102, "Student Not Found")
print("\nAccessing the value (name) of student with ID 102:")
print(student_name)

# 1.4 Creating a nested dictionary (dictionary of dictionaries)
nested_students = {
    101: {"name": "Alice", "age": 20, "grade": "A"},
    102: {"name": "Bob", "age": 21, "grade": "B"},
    103: {"name": "Charlie", "age": 22, "grade": "A"},
    104: {"name": "David", "age": 23, "grade": "C"},
    105: {"name": "Eve", "age": 24, "grade": "B"}
}
print("\nNested Dictionary:")
print(nested_students)

# 1.5 Accessing nested dictionary values
student_id = 102
student_info = nested_students.get(student_id, "Student Not Found")
print(f"\nAccessing nested dictionary for student ID {student_id}:")
print(student_info)

# 1.6 Printing all the keys (student IDs) in the dictionary
print("\nKeys in the nested dictionary:")
print(nested_students.keys())

# 1.7 Deleting a student from the dictionary
del students[105]  # Removing student with ID 105 (Eve)
print("\nDictionary after deleting student with ID 105:")
print(students)
