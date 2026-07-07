
import pandas as pd
import matplotlib.pyplot as plt

data = {
    "Time": ["6 AM", "8 AM", "10 AM", "12 PM", "2 PM", "4 PM", "6 PM"],
    "Bird Activity": [90, 80, 60, 40, 30, 50, 70],
    "Human Traffic": [10, 20, 40, 70, 90, 60, 30]
}

df = pd.DataFrame(data)

plt.plot(df["Time"], df["Bird Activity"], marker="o", label="Bird Activity")
plt.plot(df["Time"], df["Human Traffic"], marker="o", label="Human Traffic")

plt.title("Bird Activity vs Human Traffic")
plt.xlabel("Time of Day")
plt.ylabel("Activity Level")

plt.legend()

plt.show()