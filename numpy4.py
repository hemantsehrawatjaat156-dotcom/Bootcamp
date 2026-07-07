import pandas as pd
import numpy as np


df = pd.DataFrame({
    "Roll": range(1, 101),
    "Name": ["Student" + str(i) for i in range(1, 101)],
    "Python": np.random.randint(0, 101, 100),
    "Java": np.random.randint(0, 101, 100),
    "ML": np.random.randint(0, 101, 100),
    "Cloud": np.random.randint(0, 101, 100),
    "Attendance": np.random.randint(50, 101, 100)
})

df["Total"] = df["Python"] + df["Java"] + df["ML"] + df["Cloud"]

df["Percentage"] = df["Total"] / 4

def grade(x):
    if x >= 90:
        return "A+"
    elif x >= 80:
        return "A"
    elif x >= 70:
        return "B"
    elif x >= 60:
        return "C"
    elif x >= 40:
        return "D"
    else:
        return "F"

df["Grade"] = df["Percentage"].apply(grade)

df["Rank"] = df["Percentage"].rank(ascending=False).astype(int)

top10 = df.sort_values("Percentage", ascending=False).head(10)
print("Top 10 Students")
print(top10)

fail = df[
    ((df["Python"] < 40).astype(int) +
     (df["Java"] < 40).astype(int) +
     (df["ML"] < 40).astype(int) +
     (df["Cloud"] < 40).astype(int)) >= 2
]

print("\nStudents below 40 in at least 2 subjects")
print(fail)

topper = df.sort_values("Percentage", ascending=False).head(1)
print("\nDepartment Topper")
print(topper)

low_attendance = df[df["Attendance"] < 75]
print("\nAttendance below 75%")
print(low_attendance)

top10.to_csv("Topper_List.csv", index=False)

print("\nTopper List exported successfully.")

print(df)