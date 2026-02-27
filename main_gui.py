import tkinter as tk
from tkinter import ttk
import json
import data_manager

def main_window():
    global main_win , tree, columns
    main_win = tk.Tk()
    main_win.title("Main Window")
    main_win.geometry("400x300")
    main_win.configure(bg="#333333")
    main_win.update()
    w = main_win.winfo_width()
    h = main_win.winfo_height()
    ws = main_win.winfo_screenwidth()
    hs = main_win.winfo_screenheight()
    x = int((ws/2) - (w/2))
    y = int((hs/2) - (h/2))
    main_win.geometry(f"{w}x{h}+{x}+{y}")
    with open("students.json", "r") as file:
        data = json.load(file)
    columns = ("name", "id", "math", "lecture",
            "pe", "english", "chemistry",
            "programming", "web_design",
            "average", "min", "max", "gpa")
    tree = ttk.Treeview(main_win, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col.capitalize())
        tree.column(col, width=50, anchor="center")
    for student in data["students"]:
        tree.insert("", tk.END,
            values=[student.get(col, "") for col in columns])
    tree.pack(fill="both", expand=True) # fill both means it will expand in both directions, expand true means it will take all available space
    tree.bind("<Double-1>", lambda event: edit_cell(event)) # bind double click to edit cell
    entry = tk.Entry(main_win)
    entry.pack(pady=5)
    add_btn = tk.Button(
        main_win,
        text="Add Student",
        command=lambda: add_student(entry.get())
    )
    add_btn.pack()
    refresh_student()
    main_win.mainloop()
def student_window(username):
    global tree
    student_win = tk.Tk()
    student_win.title(f"{username}'s Dashboard")
    student_win.geometry("400x300")
    student_win.configure(bg="#333333")
    student_win.update()
    w = student_win.winfo_width()
    h = student_win.winfo_height()
    ws = student_win.winfo_screenwidth()
    hs = student_win.winfo_screenheight()
    x = int((ws/2) - (w/2))
    y = int((hs/2) - (h/2))
    student_win.geometry(f"{w}x{h}+{x}+{y}")
    columns = ("name", "id", "math", "lecture",
            "pe", "english", "chemistry",
            "programming", "web_design",
            "average", "min", "max", "gpa")
    tk.Label(
        student_win, text=f"Welcome, {username}!",
        font=("Arial", 24)
    ).pack(pady=50)
    with open("students.json", "r") as file:
        data = json.load(file)
    tree = ttk.Treeview(student_win, columns=columns, show="headings")
    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=30)
    for student in data["students"]:
        if student["name"] == username:
            tree.insert("", tk.END, values=(
                student["name"],
                student["id"],
                student["math"],
                student["lecture"],
                student["pe"],
                student["english"],
                student["chemistry"],
                student["programming"],
                student["web_design"],
                student["average"],
                student["min"],
                student["max"],
                student["gpa"]
            ))
    tree.pack(fill="both", expand=True) # fill both means it will expand in both directions, expand true means it will take all available space
    refresh_student_tree(username)
    student_win.mainloop()
def edit_cell(event):
    selected_item = tree.focus() # focus returns the id of the selected item
    column = tree.identify_column(event.x) # identify_column returns the column number of the clicked cell
    row = tree.identify_row(event.y) # identify_row returns the row id of the clicked cell
    if not selected_item or not column or not row:
        return # if no item is selected or no column is identified or no row is identified, return
    x, y, width, height = tree.bbox(selected_item, column) # bbox returns the bounding box of the cell
    value = tree.set(selected_item, column) # set returns the value of the cell
    entry = tk.Entry(main_win) # create an entry widget
    entry.place(x=x, y=y, width=width, height=height) # place the entry widget on top of the cell
    entry.insert(0, value) # insert the current value of the cell into the entry
    entry.focus() # focus the entry widget
    entry.bind("<Return>", lambda e: save_edit(selected_item, column, entry.get())) # bind the return key to save the edit
    entry.bind("<FocusOut>", lambda e: entry.destroy()) # bind focus out to destroy
def save_edit(selected_item, column, new_value):
    values = tree.item(selected_item)["values"]
    student_id = str(values[1])
    col_index = int(column.replace("#", "")) - 1
    column_name = columns[col_index]
    if column_name in ("average", "min", "max", "gpa"):
        return
    data_manager.update_student(student_id, column_name, new_value)
    refresh_student()
def add_student(name):
    data_manager.add_student(name)
    main_win.destroy()
    main_window()
def refresh_student():
    global tree
    for item in tree.get_children():
        tree.delete(item)
    students = data_manager.get_all_students()
    for student in students:
        avg, minimum, maximum, gpa = data_manager.calculate_stats(student)
        values = [
            student.get("name",""),
            student.get("id",""),
            student.get("math",""),
            student.get("lecture",""),
            student.get("pe",""),
            student.get("english",""),
            student.get("chemistry",""),
            student.get("programming",""),
            student.get("web_design",""),
            avg,
            minimum,
            maximum,
            gpa
        ]
        tree.insert("", tk.END, values=values)
def refresh_student_tree(username):
    global tree
    for item in tree.get_children():
        tree.delete(item)
    students = data_manager.get_all_students()
    for student in students:
        if student["name"] == username:
            avg, minimum, maximum, gpa = data_manager.calculate_stats(student)
            values = [
                student.get("name",""),
                student.get("id",""),
                student.get("math",""),
                student.get("lecture",""),
                student.get("pe",""),
                student.get("english",""),
                student.get("chemistry",""),
                student.get("programming",""),
                student.get("web_design",""),
                avg,
                minimum,
                maximum,
                gpa
            ]
            tree.insert("", tk.END, values=values)
main_window()
