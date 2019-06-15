class Employee:
    emp_count = 0
    tot_sal = 0

    def __init__(self,name, family, salary, department):
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
        print("The Employee count is :- ", Employee.tot_sal/Employee.emp_count)
        return


p1 = Employee("harish", "tata", 5000, "cs")
p2 = Employee("pallavi", "desai", 10000, "cs")
p3 = Employee("neeraj", "padarthi", 15000, "cs")
p1.employee_count()
p2.average()
