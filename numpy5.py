import pandas as pd
import numpy as np

dept = ["IT", "HR", "Finance", "Marketing", "Sales"]

df = pd.DataFrame({
    "EmpID": range(1,501),
    "Department": np.random.choice(dept,500),
    "Experience": np.random.randint(1,21,500),
    "Salary": np.random.randint(20000,100001,500),
    "Performance": np.random.randint(1,6,500)
})

df.to_csv(r"C:\Users\Heman\OneDrive\Desktop\bootcamp\employees.csv",index=False)

df.to_excel(r"C:\Users\Heman\OneDrive\Desktop\bootcamp\Employee.xlsx",index=False)

csv = pd.read_csv(r"C:\Users\Heman\OneDrive\Desktop\bootcamp\employees.csv")
excel = pd.read_excel(r"C:\Users\Heman\OneDrive\Desktop\bootcamp\Employee.xlsx")

print(csv.equals(excel))

print("\nAverage Salary Department-wise")
print(df.groupby("Department")["Salary"].mean())

highest = df[df["Performance"]==df["Performance"].max()]
print("\nHighest Performer")
print(highest)

avg_salary = df.groupby("Department")["Salary"].transform("mean")
high_salary = df[df["Salary"]>avg_salary]

print("\nSalary Greater than Department Average")
print(high_salary)

result = df[(df["Experience"]>15) & (df["Performance"]<3)]

print("\nExperience >15 and Performance <3")
print(result)

def bonus(x):
    if x >= 4:
        return x*0 + 10   

df["Bonus"] = np.where(df["Performance"]>=4,
                       df["Salary"]*0.10,
                       df["Salary"]*0.05)

bonus_emp = df[df["Bonus"]>10000]
bonus_emp.to_csv(r"C:\Users\Heman\OneDrive\Desktop\bootcamp\Employees.csv",index=False)

print("\nEmployees having Bonus >10000")
print(bonus_emp)

print("\nFinal DataFrame")
print(df)