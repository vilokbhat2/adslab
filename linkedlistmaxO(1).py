class Student:
    def __init__(self, name, program, register_number, marks):
        self.name = name
        self.program = program
        self.register_number = register_number
        self.marks = marks
class StudentInfoSystem:
    def __init__(self):
        self.students_dict = {}  # Maps register_number -> Student object
        self.students_list = []  # List to store Student objects
        self.max_student = None  # Student object with maximum marks

    # Method to add a student
    def add_student(self, name, program, register_number, marks):
        student = Student(name, program, register_number, marks)
        self.students_dict[register_number] = student
        self.students_list.append(student)
        
        # Update max_student if this student has higher marks
        if self.max_student is None or marks > self.max_student.marks:
            self.max_student = student

    # Method to search a student by registration number
    def search_student(self, register_number):
        if register_number in self.students_dict:
            student = self.students_dict[register_number]
            return vars(student)  # Return student details as a dictionary
        else:
            return None  # Student not found

    # Method to display student details with max marks in O(1)
    def get_max_marks_student(self):
        if self.max_student is None:
            return None  # No students in the system
        else:
            return vars(self.max_student)  # Return student details as a dictionary
# Create an instance of the student information system
sis = StudentInfoSystem()

# Add students
sis.add_student("Alice", "Computer Science", "CS101", 95)
sis.add_student("Bob", "Mechanical Engineering", "ME102", 88)
sis.add_student("Charlie", "Electrical Engineering", "EE103", 98)

# Search for a student by registration number
print(sis.search_student("CS101"))
# Output: {'name': 'Alice', 'program': 'Computer Science', 'register_number': 'CS101', 'marks': 95}

# Get the student with maximum marks
print(sis.get_max_marks_student())
# Output: {'name': 'Charlie', 'program': 'Electrical Engineering', 'register_number': 'EE103', 'marks': 98}
