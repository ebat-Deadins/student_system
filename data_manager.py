import json
import os

FILE_NAME = "students.json"

def initialize_file():
    if not os.path.exists(FILE_NAME):
        with open(FILE_NAME, "w") as f:
            json.dump({"students": []}, f, indent=4)

def load_data():
    initialize_file()
    try:
        with open(FILE_NAME, "r") as f:
            data = json.load(f)
            if "students" not in data:
                data = {"students": []}
            return data
    except json.JSONDecodeError:
        return {"students": []}

def save_data(data):
    with open(FILE_NAME, "w") as f:
        json.dump(data, f, indent=4)

def generate_id(data):
    if not data["students"]:
        return "1"
    # numeric ID only
    ids = []
    for student in data["students"]:
        try:
            ids.append(int(student["id"]))
        except:
            pass
    return str(max(ids)+1 if ids else 1)

def add_student(name):
    if not name:
        return
    data = load_data()
    new_student = {
        "name": name,
        "id": generate_id(data),
        "math": 0,
        "lecture": 0,
        "pe": 0,
        "english": 0,
        "chemistry": 0,
        "programming": 0,
        "web_design": 0,
        "average": 0,
        "min":0,
        "max":0,
        "gpa":0
    }
    data["students"].append(new_student)
    save_data(data)

def update_student(student_id, column_name, new_value):
    data = load_data()
    for student in data["students"]:
        if student["id"] == student_id:
            if column_name in student:
                try:
                    student[column_name] = float(new_value)
                except:
                    student[column_name] = new_value
            break
    save_data(data)

def get_all_students():
    return load_data()["students"]

def get_student_by_name(name):
    for s in get_all_students():
        if s["name"] == name:
            return s
    return None

def calculate_stats(student):
    subjects = ["math","lecture","pe","english","chemistry","programming","web_design"]
    grades = []
    for sub in subjects:
        try:
            grades.append(float(student.get(sub,0)))
        except:
            grades.append(0)
    if not grades:
        return 0,0,0,0
    avg = round(sum(grades)/len(grades),2)
    minimum = min(grades)
    maximum = max(grades)
    if avg >= 90:
        gpa = 4.0
    elif avg >= 80:
        gpa = 3.0
    elif avg >= 70:
        gpa = 2.0
    elif avg >= 60:
        gpa = 1.0
    else:
        gpa = 0.0
    return avg, minimum, maximum, gpa
