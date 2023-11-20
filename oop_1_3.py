class Person:
    def __init__(self, name, age, address):
        self.name = name
        self.age = age
        self.address = address

    def display_info(self):
        print(f"Ismi: {self.name}, Yosh: {self.age}, Manzil: {self.address}")

class Student(Person):
    def __init__(self, name, age, address, student_id):
        super().__init__(name, age, address)
        self.student_id = student_id

    def display_info(self):
        super().display_info()
        print(f"Student ID: {self.student_id}")

class Teacher(Person):
    def __init__(self, name, age, address, employee_id):
        super().__init__(name, age, address)
        self.employee_id = employee_id

    def display_info(self):
        super().display_info()
        print(f"Employee ID: {self.employee_id}")

# Test qismi
person = Person("John Doe", 30, "123 Main St")
student = Student("Alice Smith", 20, "456 Oak St", "S12345")
teacher = Teacher("Mr. Johnson", 45, "789 Pine St", "T98765")

person.display_info()
print("\n")
student.display_info()
print("\n")
teacher.display_info()

if __name__ == '__main__':
    pass