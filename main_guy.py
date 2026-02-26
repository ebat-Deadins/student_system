import tkinter
from tkinter import messagebox
def main_window():
    main_win = tkinter.Tk()
    main_win.title("Main Window")
    main_win.geometry('400x300')
    main_win.configure(bg='#333333')

    welcome_label = tkinter.Label(
        main_win, text="Welcome to the Main Window!", bg='#333333', fg="#FF3399", font=("Arial", 20))
    welcome_label.pack(pady=100)

    main_win.mainloop()

