import tkinter
from tkinter import messagebox
import data_manager

def main_window():
    main_win = tkinter.Tk()
    main_win.title("Main Window")
    main_win.geometry('400x300')
    main_win.configure(bg='#333333')

    welcome_label = tkinter.Label(
        main_win, text="Welcome to the Main Window!", bg='#333333', fg="#FF3399", font=("Arial", 20))
    welcome_label.pack(pady=100)
    frame = tkinter.Frame(bg='#333333')
    students_label = tkinter.Label(
    frame, text="Students", bg='#333333', fg="#FFFFFF", font=("Arial", 16))
    students_label.grid(row=2, column=0, pady=20)
    frame.pack()
    main_win.mainloop()


