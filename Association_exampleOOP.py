class Student:
    def __init__(self, name):
        self.name = name

    def enroll(self, course):
        self.course = course
    def show_course(self):
        print(f"{self.name} is enrolled in {self.course.name}")

class Course:
    def __init__(self, name):
        self.name = name

#Instances
student = Student("Carlos")
course = Course("Python Programming")

student.enroll(Course)