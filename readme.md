📘 Student Report Card Generator (Python Project)

A simple and fully functional Python console application to manage student details, store marks, calculate grades, and generate report cards.
This project uses JSON file storage, Object-Oriented Programming (OOP), and file handling concepts.

🚀 Features

✔ Add new students
✔ Add or update subject marks
✔ Auto-calculation of Total, Average, and Grade
✔ View an individual student’s report
✔ List all students with summary table
✔ Delete a student
✔ Data automatically saved in students.json
✔ Uses classes, objects, error handling, file handling, and JSON

🛠 Technologies Used

Python 3

Object-Oriented Programming

JSON file storage

File handling (open, read/write)

Error handling (try-except)

📂 File Structure
student-report-card/
│
├── students.json      # Auto-created file for storing student data
├── report_card.py     # Main application code
└── README.md          # Documentation

📥 How to Run

Install Python 3

Download or clone this repository

Run the program:

python report_card.py

📌 Menu Options

When you start the program, you will see:

=== STUDENT REPORT CARD ===
1. Add student
2. Add/Update marks
3. List students (summary)
4. View student report
5. Delete student
6. Exit


You can choose any option by typing the menu number.

📊 Example Output (Summary)
Roll    Name        Total   Avg     Grade
1       Kannan      245     81.67   A
2       Pravin      175     58.33   D

🧮 How Grades Are Calculated
Average Marks	Grade
≥ 90	A+
≥ 80	A
≥ 70	B
≥ 60	C
≥ 50	D
< 50	F
📘 Concepts You Learn in This Project

This project helps you understand:

Classes & objects

__init__ method

Instance variables

Storing objects in JSON

Converting objects to dictionaries

Reading & writing files

Loops

Conditional logic

Guard clauses (early return)

Error handling

Clean code structure

Searching in a list (linear search)

Perfect for starting OOP + File Handling + JSON in Python.

🧑‍💻 Author

Kannan
Beginner Python developer exploring OOP, automation, and full-stack development.

⭐ If you like this project

Feel free to star the repo or improve the code!