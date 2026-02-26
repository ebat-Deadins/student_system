import tkinter as tk
from tkinter import ttk
import json
import data_manager

def main_window():
    global main_win
    main_win = tk.Tk()
    main_win.title("Main Window")
    main_win.geometry("400x300")
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

    columns = ("Name", "ID", "Math", "Lecture")
    tree = ttk.Treeview(main_win, columns=columns, show="headings")

    for col in columns:
        tree.heading(col, text=col)
        tree.column(col, width=30)

    for student in data["students"]:
        tree.insert("", tk.END, values=(
            student["name"],
            student["id"],
            student["math"],
            student["lecture"]
        ))

    tree.pack(fill="both", expand=True)

    entry = tk.Entry(main_win)
    entry.pack(pady=5)

    add_btn = tk.Button(
        main_win,
        text="Add Student",
        command=lambda: add_student(entry.get())
    )
    add_btn.pack()

    main_win.mainloop()


def add_student(name):
    data_manager.add_student_1(name)
    main_win.destroy()
    main_window()


main_window()
