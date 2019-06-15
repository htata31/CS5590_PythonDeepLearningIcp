class Employee:
    emp_count = 0
    tot_sal = 0

    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.dept = department
        Employee.emp_count += 1
        Employee.tot_sal += salary

    @staticmethod
    def employee_count():
        print("The Employee count is :- ", Employee.emp_count)

    @staticmethod
    def average():
        print("The Average salary is :- ", Employee.tot_sal/Employee.emp_count)


class Fulltime_Employee(Employee):
    def __init__(self, name, family, salary, department, grad_year):
        Employee.__init__(self, name, family, salary, department)
        self.grad_year = grad_year
        Employee("Tejaswi", "koppuravuri", 50000, "cs")
        Employee("pallavi", "desai", 10000, "cs")
        Employee("neeraj", "padarthi", 15000, "cs")

    def employee_info(self):
        print("Employee Info :--")
        print("The first and the family name is", self.name, self.family)
        print("From", self.dept, "department", "and their respective salary is ", self.salary)
        print("Graduated at", self.grad_year)


emp1 = Fulltime_Employee("Harish", "Tata", 5000, "cs", 2015)
Fulltime_Employee.employee_count()
Fulltime_Employee.average()
emp1.employee_info()


