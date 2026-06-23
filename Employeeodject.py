class Employee:
    def __init__(self, name, department="General", bonus=0):
        self.name = name
        self.department = department
        self.bonus = bonus

    def annual_summary(self):
        fixed_salary = 30000
        total_pay = fixed_salary + self.bonus

        print(f"Employee Name : {self.name}")
        print(f"Department    : {self.department}")
        print(f"Total Pay     : {total_pay}")
        print("-" * 30)


emp1 = Employee("Hemant", "IT", 5000)

emp2 = Employee("Rahul", "HR", 10000)

emp3 = Employee("Priya", "Finance", 7500)

emp1.annual_summary()
emp2.annual_summary()
emp3.annual_summary()