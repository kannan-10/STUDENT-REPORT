import json
import os

DATA_FILE = 'student_report_card.json'

class  Student:
    def __init__(self, roll, name, age, marks=None):
        self.roll = roll
        self.name = name
        self.age = age
        self.marks = marks or {}

    def to_dict(self):
        return {
            "roll": self.roll,
            "name": self.name,
            "age": self.age,
            "marks": self.marks
        }

    @staticmethod
    def from_dict(d):
        return Student(d.get("roll"), d.get("name"), d.get("age"), d.get("marks"))

    def total(self):
        return sum(self.marks.values()) if self.marks else 0

    def average(self):
        if not self.marks:
            return 0
        return self.total() / len(self.marks)

    def grade(self):
        avg = self.average()

        if avg > 90:
            return "+A"
        if avg > 80:
            return "A"
        if avg > 70:
            return "B"
        return "C"
    
    class StudentReportCard:
        def __init__(self, filepath=DATA_FILE):
            self.filepath = filepath
            self.students = self.load_students()
    
        def load_students(self):
            if not os.path.exists(self.filepath):
                return []
            try:
                with open(self.filepath, 'r', encoding='utf-8') as f:
                    data = json.load(f)
                return [Student.from_dict(d) for d in data]
            except (json.JSONDecodeError, OSError):
                return []
    
        def save_students(self):
            try:
                with open(self.filepath, 'w', encoding='utf-8') as f:
                    json.dump([s.to_dict() for s in self.students], f, indent=2)
            except OSError:
                pass
    
        def add_student(self, student):
            self.students.append(student)
            self.save_students()
    
        def get_student(self, roll):
            for student in self.students:
                if student.roll == roll:
                    return student
            return None
    
        def main_menu(self):
            while True:
                print("\nStudent Report Card System")
                print("1. Add Student")
                print("2. View Student Report") 
                print("3. Exit")
                choice = input("Enter your choice: ")
    
                if choice == '1':
                    roll = input("Enter your roll no: ").strip()
                    name = input("Enter your name: ").strip()
                    age = input("Enter your age: ").strip()
                    marks = {}
                    subjects = input("Enter subjects separated by comma: ").split(',')
                    for subject in subjects:
                        mark = input(f"Enter marks for {subject.strip()}: ").strip()
                        marks[subject.strip()] = int(mark)
                    student = Student(roll, name, age, marks)
                    self.add_student(student)
                    print("Student added.\n")
                elif choice == '2':
                    roll = input("Enter your roll no: ").strip()
                    student = self.get_student(roll)
                    if student:
                        print(f"Name: {student.name}")
                        print(f"Age: {student.age}")
                        print(f"Marks: {student.marks}")
                        print(f"Grade: {student.grade()}")
                    else:
                        print("Student not found.\n")
                elif choice == '3':
                    roll = input("Enter the roll to delete: ").strip()
                    student = self.get_student(roll)
                    if student:
                        self.students.remove(student)
                        self.save_students()
                        print("Student has been deleted.\n")
                    else:
                        print("Student not found.\n")
                else:
                    print("Invalid choice. Please try again.")
    
    if __name__ == "__main__":
        StudentReportCard().main_menu()


            
                


        

            