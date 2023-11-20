class Subject:
    def __init__(self, name, credits):
        self.name = name
        self.credits = credits

    def display_info(self):
        print(f"Fanni nomi: {self.name}, Kreditlar soni: {self.credits}")

class Student:
    def __init__(self, name, student_id):
        self.name = name
        self.student_id = student_id
        self.subjects = []

    def enroll_subject(self, subject):
        self.subjects.append(subject)
        print(f"{self.name} fanga yozildi: {subject.name}")

    def display_info(self):
        print(f"Talaba: {self.name}, Talaba ID: {self.student_id}")
        print("Fanalari:")
        for subject in self.subjects:
            subject.display_info()

# Test qismi
math_subject = Subject("Math", 4)
physics_subject = Subject("Physics", 3)

student = Student("John Doe", "S12345")
student.enroll_subject(math_subject)
student.enroll_subject(physics_subject)
student.display_info()


if __name__ == '__main__':
    pass