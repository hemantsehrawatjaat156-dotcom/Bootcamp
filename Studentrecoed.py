class Student:
    __count = 0  

    def __init__(self, roll_no, marks: list, grade):
        self.__roll_no = roll_no
        self.__marks = marks        
        self._grade = grade        
        Student.__count += 1

    def gpa(self):
        return sum(self.__marks) / (len(self.__marks) * 10)

    def gpa(self, marks):
        for m in marks:
            if not (0 <= m <= 100):
                raise ValueError(f"Mark {m} is out of range (0-100)")
        self.__marks = marks

    def count(cls):
        return cls.__count

    def __str__(self):
        return f"Roll No: {self.__roll_no} | GPA: {self.gpa:.2f} | Grade: {self._grade}"

s1 = Student(101, [85, 90, 78], 'A')
s2 = Student(102, [60, 70, 55], 'B')
print(s1)
print(s2)
print("Total Students:", Student.count())

s1.gpa = [95, 88, 92]   
print("Updated GPA:", s1.gpa)