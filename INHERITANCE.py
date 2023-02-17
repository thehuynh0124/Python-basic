class Employee:
    co_salary = 1.04
    def __int__(self, firstName, lastName, pay):
        self.firstName = firstName
        self.lastName = lastName
        self.pay = pay
        self.email = firstName + "." + lastName + "@gmail.com"
    def fullName(self):
        return "{} {}".format(self.firstName, self.lastName)
    def apply_co_salary(self):
        self.pay = float(self.pay * self.co_salary)
        return self.pay

    #special methods
    def __repr__(self):     #in ra cả thư viện được sử dụng, phục vụ cho dev
        return f"Employee {self.firstName} {self.lastName}, {self.pay}"
    def __str__(self):
        return f"{self.fullName()} - {self.email}"
    def __add__(self, other):
        return self.pay + other.pay

class Deverloper(Employee):
    co_salary = 1.06
    def __init__(self, firstName, lastName, pay, language):
        super().__int__(firstName, lastName, pay)
        self.language = language

class Manager(Employee):
    co_salary = 1.2
    def __init__(self,firstName, lastName, pay, employees = None):
        super().__int__(firstName, lastName, pay)
        if employees == None:
            self.employess = []
        else:
            self.employess = employees
    def add_employees(self, emp):
        if emp not in self.employess:
            self.employess.append(emp)
    def remove_employees(self, emp):
        if emp in self.employess:
            self.employess.remove(emp)
    def print_employees(self):
        for emp in self.employess:
            print("-->", emp.fullName())


dev1 = Deverloper("Huynh", "Vu", 800, "python")
dev2 = Deverloper("Hung", "Nguyen", 500, "Java")
manager1 = Manager('Đại', 'Phạm', 800, [dev1, dev2])
#manager1.remove_employees(dev1)
#manager1.add_employees(dev1)
#manager1.print_employees()
#print(manager1.fullName())
#print(manager1.apply_co_salary())
print(dev2.fullName())
#print(dev1.apply_co_salary())
#print(str(dev1))
#print(repr(dev1))
