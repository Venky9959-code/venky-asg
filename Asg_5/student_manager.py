import json
import os
import re

FILE_NAME = "student_records.json"


# ---------------- Load Data ----------------
def load_students():
    if os.path.exists(FILE_NAME):
        try:
            with open(FILE_NAME, "r") as file:
                return json.load(file)
        except:
            return []
    return []


# ---------------- Save Data ----------------
def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)


# ---------------- Email Validation ----------------
def valid_email(email):
    pattern = r'^[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}$'
    return re.fullmatch(pattern, email)


# ---------------- Add Student ----------------
def add_student():

    students = load_students()

    try:
        sid = int(input("Enter Student ID : "))
        name = input("Enter Student Name : ").title()
        email = input("Enter Email : ")

        if not valid_email(email):
            raise ValueError("Invalid Email Format!")

        # Duplicate ID Check
        for student in students:
            if student["ID"] == sid:
                print("Student ID Already Exists!")
                return

        student = {
            "ID": sid,
            "Name": name,
            "Email": email
        }

        students.append(student)

        save_students(students)

        print("\nStudent Added Successfully!\n")

    except ValueError as e:
        print("Error :", e)


# ---------------- View Students ----------------
def view_students():

    students = load_students()

    if len(students) == 0:
        print("\nNo Student Records Found!\n")
        return

    print("\n" + "=" * 50)
    print("         STUDENT RECORDS")
    print("=" * 50)

    for student in students:
        print(f"ID    : {student['ID']}")
        print(f"Name  : {student['Name']}")
        print(f"Email : {student['Email']}")
        print("-" * 50)


# ---------------- Main Menu ----------------
while True:

    print("\n========== Student Record Manager ==========")
    print("1. Add Student")
    print("2. View Students")
    print("3. Exit")

    try:

        choice = int(input("Enter Your Choice : "))

        if choice == 1:
            add_student()

        elif choice == 2:
            view_students()

        elif choice == 3:
            print("\nThank You!")
            break

        else:
            print("Choose Between 1 - 3")

    except ValueError:
        print("Please Enter Numbers Only!")