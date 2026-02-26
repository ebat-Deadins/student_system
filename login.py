import tkinter
from tkinter import messagebox
import main_guy

window = tkinter.Tk()
window.title("Login form")
window.geometry('340x440')
window.configure(bg='#333333')


# 🔹 USERS
student_password = "12345"   # all students use this
admin_password = "admin999"  # admin uses different password


# 🔹 Login function
def login():
    username = username_entry.get()
    password = password_entry.get()

    # Admin check
    if username == "admin" and password == admin_password:
        window.destroy()
        main_guy.main_window()

    # Student check (any name but same password)
    elif username != "admin" and password == student_password:
        messagebox.showinfo("Login Success", f"Student {username} logged in.")

    else:
        messagebox.showerror("Error", "Invalid login.")


frame = tkinter.Frame(bg='#333333')

# Widgets
login_label = tkinter.Label(
    frame, text="Login", bg='#333333', fg="#FF3399", font=("Arial", 30))

username_label = tkinter.Label(
    frame, text="Username", bg='#333333', fg="#FFFFFF", font=("Arial", 16))

username_entry = tkinter.Entry(frame, font=("Arial", 16))

password_label = tkinter.Label(
    frame, text="Password", bg='#333333', fg="#FFFFFF", font=("Arial", 16))

password_entry = tkinter.Entry(frame, show="*", font=("Arial", 16))

login_button = tkinter.Button(
    frame, text="Login", bg="#FF3399", fg="#FFFFFF",
    font=("Arial", 16), command=login)


# Layout
login_label.grid(row=0, column=0, columnspan=2, pady=40)
username_label.grid(row=1, column=0)
username_entry.grid(row=1, column=1, pady=20)
password_label.grid(row=2, column=0)
password_entry.grid(row=2, column=1, pady=20)
login_button.grid(row=3, column=0, columnspan=2, pady=30)

frame.pack()
window.mainloop()
