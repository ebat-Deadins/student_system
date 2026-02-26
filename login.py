import tkinter
from tkinter import messagebox
import main_gui
import json
def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()
    with open("students.json", "r") as f:
        students = json.load(f)
    if not username or not password:
        messagebox.showerror("Error", "Please fill all fields.")
        return
    # Admin
    if username == "admin" and password == "admin999":
        messagebox.showinfo("Login Success", "Admin logged in.")
        window.withdraw()
        main_gui.main_window()
    # Student
    elif username in [student["name"] for student in students["students"]]:
        for student in students["students"]:
            if student["name"] == username and password == student["id"]:  # Assuming all students have the same password (their ID)
                messagebox.showinfo("Login Success", f"Student {username} logged in.")
                window.withdraw()
        main_gui.student_window(username=username)
    else:
        messagebox.showerror("Error", "Invalid login.")
window = tkinter.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')
frame = tkinter.Frame(window, bg='#333333')
frame.pack(pady=50)
tkinter.Label(
    frame, text="Login",
    bg='#333333', fg="#FF3399",
    font=("Arial", 30)
).grid(row=0, column=0, columnspan=2, pady=30)
tkinter.Label(
    frame, text="Username",
    bg='#333333', fg="#FFFFFF",
    font=("Arial", 16)
).grid(row=1, column=0)
username_entry = tkinter.Entry(frame, font=("Arial", 16))
username_entry.grid(row=1, column=1, pady=15)
tkinter.Label(
    frame, text="Password",
    bg='#333333', fg="#FFFFFF",
    font=("Arial", 16)
).grid(row=2, column=0)
password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))
password_entry.grid(row=2, column=1, pady=15)
tkinter.Button(
    frame,
    text="Login",
    bg="#FF3399",
    fg="#FFFFFF",
    font=("Arial", 16),
    command=login
).grid(row=3, column=0, columnspan=2, pady=30)
window.mainloop()
