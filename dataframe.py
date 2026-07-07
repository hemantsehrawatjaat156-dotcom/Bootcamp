import pandas as pd

data = {
    'Name': ['Alice', 'Bob', 'Charlie', 'David', 'Eva'],
    'Age': [25, 30, 35, 40, 45],
    'Department': ['HR', 'Finance', 'IT', 'Marketing', 'Sales'],
}

df = pd.DataFrame(data)
print(df)

print(df['Name'])

df['Salary'] = [50000, 60000, 70000, 80000, 90000]
print(df)

