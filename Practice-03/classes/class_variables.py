class Employee:
    company = "Tech Corp"
    employee_count = 0
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.employee_count += 1
    
    def display_info(self):
        print(f"{self.name} works at {Employee.company}")

class Student:
    school = "Central High"
    total_students = 0
    
    def __init__(self, name, grade):
        self.name = name
        self.grade = grade
        Student.total_students += 1

emp1 = Employee("Alice", 50000)
emp2 = Employee("Bob", 60000)
emp1.display_info()
emp2.display_info()
print(Employee.company)
print(Employee.employee_count)

s1 = Student("Charlie", "A")
s2 = Student("Diana", "B")
print(Student.school)
print(Student.total_students)