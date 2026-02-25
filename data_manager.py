### This file handles: Loading data Saving data Adding students Deleting students Searching students Updating student ⚠️ No Tkinter code here. ⚠️ No GUI elements. Only logic + file handling.###
import json
import os

FILE_NAME = "students.json"


# -------------------------
# Load Data
# -------------------------
def load_data():
    """Load student data from JSON file."""
    if not os.path.exists(FILE_NAME):
        return {}

    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except json.JSONDecodeError:
        return {}


# -------------------------
# Save Data
# -------------------------
def save_data(data):
    """Save student data to JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


# -------------------------
# Add Student
# -------------------------
def add_student(student_id, name, age, course):
    data = load_data()

    if student_id in data:
        return False, "Student ID already exists."

    data[student_id] = {
        "name": name,
        "age": age,
        "course": course
    }

    save_data(data)
    return True, "Student added successfully."


# -------------------------
# Delete Student
# -------------------------
def delete_student(student_id):
    data = load_data()

    if student_id not in data:
        return False, "Student not found."

    del data[student_id]
    save_data(data)

    return True, "Student deleted successfully."


# -------------------------
# Update Student
# -------------------------
def update_student(student_id, name, age, course):
    data = load_data()

    if student_id not in data:
        return False, "Student not found."

    data[student_id] = {
        "name": name,
        "age": age,
        "course": course
    }

    save_data(data)

    return True, "Student updated successfully."


# -------------------------
# Search Student
# -------------------------
def search_student(student_id):
    data = load_data()

    if student_id in data:
        return True, data[student_id]

    return False, "Student not found."


# -------------------------
# Get All Students
# -------------------------
def get_all_students():
    return load_data()
