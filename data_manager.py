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
        file.truncate()
        json.dump(data, file, indent=4)


def add_grade(student_id, subject, grade):
    with open("students.json", "r+") as file:
        data = json.load(file)

        for student in data["students"]:
            if student["id"] == student_id:
                student[subject] = grade
                break

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)


def update_student(selected_item, column, new_value):
    with open("students.json", "r+") as file:
        data = json.load(file)

        for student in data["students"]:
            if student["id"] == selected_item:
                if column == "#1":
                    student["name"] = new_value
                elif column == "#2":
                    student["id"] = new_value
                elif column == "#3":
                    student["math"] = new_value
                elif column == "#4":
                    student["lecture"] = new_value
                break

        file.seek(0)
        file.truncate()
        json.dump(data, file, indent=4)

        print(f"Updated student {selected_item} - {column} set to {new_value}")
