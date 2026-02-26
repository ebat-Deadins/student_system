import tkinter as tk
from tkinter import messagebox
import main_gui
import json

def save_logged_student(username):
    try:
        with open("logged_students.json", "r") as f:
            data = json.load(f)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []

    if username not in data:
        data.append(username)

    with open("logged_students.json", "w") as f:
        json.dump(data, f, indent=4)

def login():
    username = username_entry.get().strip()
    password = password_entry.get().strip()

    if not username or not password:
        messagebox.showerror("Error", "Please fill all fields.")
        return

    try:
        with open("users.json", "r") as f:
            data = json.load(f)
            users = data["users"]
    except (FileNotFoundError, json.JSONDecodeError):
        messagebox.showerror("Error", "Users database not found or invalid.")
        return

    # Find user in array
    user = next((u for u in users if u["name"] == username), None)

    if user and user["password"] == password:
        role = user.get("role", "student")
        messagebox.showinfo("Login Success", f"{role.capitalize()} {username} logged in.")
        save_logged_student(username)
        window.withdraw()
        main_gui.main_window(role=role, username=username)
    else:
        messagebox.showerror("Error", "Invalid username or password.")

# ------------------ UI ------------------
window = tk.Tk()
window.title("Login Form")
window.geometry('340x440')
window.configure(bg='#333333')

frame = tk.Frame(window, bg='#333333')
frame.pack(pady=50)

tk.Label(frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30)).grid(row=0, column=0, columnspan=2, pady=30)
tk.Label(frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).grid(row=1, column=0)
username_entry = tk.Entry(frame, font=("Arial", 16))
username_entry.grid(row=1, column=1, pady=15)
tk.Label(frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16)).grid(row=2, column=0)
password_entry = tk.Entry(frame, show="*", font=("Arial", 16))
password_entry.grid(row=2, column=1, pady=15)
tk.Button(frame, text="Login", bg="#FF3399", fg="#FFFFFF", font=("Arial", 16), command=login).grid(row=3, column=0, columnspan=2, pady=30)

window.mainloop()
