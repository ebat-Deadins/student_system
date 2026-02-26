import json

def add_student_1(name):
    if not name:
        return

    new_student = {
        "name": name,
        "id": "0",
        "math": "0",
        "lecture": "0"
    }

    with open("students.json", "r+") as file:
        data = json.load(file)
        data["students"].append(new_student)
        file.seek(0)
        json.dump(data, file, indent=4)
