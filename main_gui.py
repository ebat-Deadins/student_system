import tkinter as tk
from tkinter import ttk
import json
import data_manager

def main_window():
    global main_win , tree
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
        tree.insert("", tk.END, values=( #"" n root level is empty string, tk.END means insert at the end of the tree
            student["name"],
            student["id"],
            student["math"],
            student["lecture"]
        ) )

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

    main_win.mainloop()

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
    # Get real student ID from tree values
    values = tree.item(selected_item)["values"]
    student_id = str(values[1])  # ID column
    # Update Treeview
    tree.set(selected_item, column, new_value)
    # Update JSON correctly
    data_manager.update_student(student_id, column, new_value)
    main_win.focus() # return focus to main window after editing
def add_student(name):
    data_manager.add_student_1(name)
    main_win.destroy()
    main_window()


main_window()
