# Hospital Patient Management System

class Student:
    def __init__(self, name):
        self.name = name
        self.grades = {}

    def add_grade(self, subject, grade):
        self.grades[subject] = grade

class Classroom:
    def __init__(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def display_students(self):
        if not self.students:
            print("No students in the classroom.")
        else:
            for student in self.students:
                print(f"Name: {student.name}, Grades: {student.grades}")

    def get_student_average(self, student_name):
        for student in self.students:
            if student.name == student_name:
                if not student.grades:
                    print(f"{student.name} has no grades.")
                    return
                average = sum(student.grades.values()) / len(student.grades)
                print(f"Average grade for {student.name}: {average}")
                return
        print("Student not found.")

    def get_class_average(self, subject):
        total, count = 0, 0
        for student in self.students:
            if subject in student.grades:
                total += student.grades[subject]
                count += 1
        if count == 0:
            print(f"No grades recorded for {subject}.")
        else:
            print(f"Class average for {subject}: {total / count}")

def main():
    classroom = Classroom()
    while True:
        print("\nSchool Class Management System")
        print("1. Add a new student")
        print("2. Display all students")
        print("3. Get average grade of a student")
        print("4. Get class average for a subject")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter student's name: ")
            student = Student(name)
            classroom.add_student(student)
            while True:
                subject = input("Enter subject (or 'done' to finish): ")
                if subject == 'done':
                    break
                grade = float(input(f"Enter grade for {subject}: "))
                student.add_grade(subject, grade)
        elif choice == '2':
            classroom.display_students()
        elif choice == '3':
            student_name = input("Enter the student's name: ")
            classroom.get_student_average(student_name)
        elif choice == '4':
            subject = input("Enter the subject: ")
            classroom.get_class_average(subject)
        elif choice == '5':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
