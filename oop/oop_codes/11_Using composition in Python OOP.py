class Salary:
    def __init__(self, pay, bonus):
        self.pay = pay
        self.bonus = bonus

class Employee:
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary

s = Salary(15000, 5000)
e = Employee("Ashwin", s)
print(e.salary.pay)