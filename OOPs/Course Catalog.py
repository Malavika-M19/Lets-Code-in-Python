# Base class Course
class Course:
    def __init__(self, course_code, course_name, credit_hours):
        self.course_code = course_code
        self.course_name = course_name
        self.credit_hours = credit_hours

    def __str__(self):
        return f"{self.course_code}: {self.course_name} ({self.credit_hours} credit hours)"


# Subclass CoreCourse, which inherits from Course
class CoreCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, required_for_major):
        # Call the constructor of the parent class
        super().__init__(course_code, course_name, credit_hours)
        self.required_for_major = required_for_major

    def __str__(self):
        required_status = "Required" if self.required_for_major else "Not Required"
        return f"{super().__str__()} - Core Course ({required_status} for major)"


# Subclass ElectiveCourse, which inherits from Course
class ElectiveCourse(Course):
    def __init__(self, course_code, course_name, credit_hours, elective_type):
        # Call the constructor of the parent class
        super().__init__(course_code, course_name, credit_hours)
        self.elective_type = elective_type

    def __str__(self):
        return f"{super().__str__()} - Elective Course (Type: {self.elective_type})"


# CoreCourse objects
core_course_1 = CoreCourse("CS101", "Introduction to Computer Science", 3, True)
core_course_2 = CoreCourse("MATH101", "Calculus I", 4, False)

# Creating ElectiveCourse objects
elective_course_1 = ElectiveCourse("HIST101", "World History", 3, "Liberal Arts")
elective_course_2 = ElectiveCourse("CS201", "Data Structures", 3, "Technical")

# Printing course information
print(core_course_1)
print(core_course_2)
print(elective_course_1)
print(elective_course_2)
