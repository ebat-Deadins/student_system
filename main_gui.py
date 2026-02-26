import tkinter as tk
from tkinter import ttk
import json
import data_manager  # your file managing students.json updates

def main_window(role="admin", username=""):
    global main_win, tree
    main_win = tk.Toplevel()  # use Toplevel instead of Tk
    main_win.title("Main Window")
    main_win.geometry("500x400")
    main_win.configure(bg="#333333")

    # Center window
    main_win.update()
    w = main_win.winfo_width()
    h = main_win.winfo_height()
    ws = main_win.winfo_screenwidth()
    hs = main_win.winfo_screenheight()
    x = int((ws/2) - (w/2))
    y = int((hs/2) - (h/2))
    main_win.geometry(f"{w}x{h}+{x}+{y}")

    # Load JSON
    with open("students.json", "r") as file:
        data = json.load(file)

    columns = ("ID", "Name", "Math", "Lecture")
    tree = ttk.Treeview(main_win, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=100)

    for student in data["students"]:
        # For students, show only their row
        if role == "student" and student["name"] != username:
            continue
        tree.insert("", tk.END, values=(
            student["id"],
            student["name"],
            student.get("math", ""),
            student.get("lecture", "")
        ))

    tree.pack(fill="both", expand=True, pady=10)

    if role == "admin":
        # Admin can add students
        entry_name = tk.Entry(main_win)
        entry_name.pack(pady=5)
        tk.Button(main_win, text="Add Student", bg="#FF3399", fg="#FFF",
                  command=lambda: add_student(entry_name.get())).pack(pady=5)

        # Admin can edit grades
        tree.bind("<Double-1>", lambda event: edit_cell(event))

def edit_cell(event):
    selected_item = tree.focus()
    column = tree.identify_column(event.x)
    row = tree.identify_row(event.y)
    if not selected_item or not column or not row:
        return
    x, y, width, height = tree.bbox(selected_item, column)
    value = tree.set(selected_item, column)
    entry = tk.Entry(main_win)
    entry.place(x=x, y=y, width=width, height=height)
    entry.insert(0, value)
    entry.focus()
    entry.bind("<Return>", lambda e: save_edit(selected_item, column, entry.get()))
    entry.bind("<FocusOut>", lambda e: entry.destroy())

def save_edit(selected_item, column, new_value):
    values = tree.item(selected_item)["values"]
    student_id = str(values[0])  # ID column
    tree.set(selected_item, column, new_value)
    data_manager.update_student(student_id, column, new_value)
    main_win.focus()

def add_student(name):
    data_manager.add_student_1(name)
    main_win.destroy()
    main_window(role="admin")
