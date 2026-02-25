# 🎓 Student ID Management System

A simple Student ID Management System built with Python and Tkinter.

This project allows administrators and staff to manage student records using a graphical user interface (GUI). The system supports authentication, student data management, and role-based access control.

---

## 📌 Project Overview

This application is designed to:

- Manage student records (Add, Search, Delete, Update)
- Store student data using JSON files
- Implement user authentication (Admin / Staff)
- Maintain clean architecture with separated logic layers

The project follows a modular structure to ensure maintainability, readability, and scalability.

---

## 🏗 Project Structure

student_system/
│
├── main_gui.py # Main application interface
├── login.py # Login window
├── data_manager.py # Backend logic for student data
├── validation.py # Input validation logic
├── students.json # Student database
├── users.json # User login database


---

## 🧠 Architecture Design

The system follows separation of concerns:

### 1️⃣ data_manager.py
Handles:
- Loading student data
- Saving student data
- Adding students
- Deleting students
- Searching students
- Updating students

⚠️ No GUI code  
⚠️ Only file handling and logic  

---

### 2️⃣ validation.py
Handles:
- Checking empty fields
- Ensuring age is numeric
- Validating student ID format

⚠️ No GUI  
⚠️ No file operations  

---

### 3️⃣ login.py
Handles:
- User authentication
- Role detection (admin / staff)

Reads from `users.json`.

---

### 4️⃣ main_gui.py
Handles:
- Building Tkinter interface
- Button actions
- Connecting GUI to backend logic

⚠️ No direct JSON manipulation  
⚠️ Uses functions from other modules  

---

## 🔐 Authentication System

Users are stored in `users.json':

.json
{
    "admin1": {
        "password": "1234",
        "role": "admin"
    },
    "staff1": {
        "password": "abcd",
        "role": "staff"
    }
}


Roles

Admin

Full access

Can add, delete, search, update students

Staff

Limited access

Cannot delete (if restricted in GUI)

{
    "101": {
        "name": "John",
        "age": "20",
        "course": "Computer Science"
    }
}
How to Run

Clone the repository:

git clone <your-repo-link>

Navigate into the folder:

cd student_system

Run the application:

python login.py
