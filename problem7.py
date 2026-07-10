import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "Date": pd.date_range("2025-01-01", periods=30),
    "Usage":[20,22,25,23,24,26,28,30,27,25,24,26,28,29,31,30,32,34,33,31,30,29,28,27,26,25,24,23,22,21]
})


df["Hour"] = 12
df["Month"] = df["Date"].dt.month
df["Day"] = df["Date"].dt.day_name()

pivot = df.pivot_table(values="Usage",
                       index="Month",
                       columns="Hour",
                       aggfunc="mean")

print(pivot)


signal = np.fft.fft(df["Usage"].values)

print("\nFFT Signal")
print(signal)


plt.plot(df["Date"], df["Usage"])
plt.plot(df["Date"], df["Usage"].rolling(window=5).mean())
plt.title("Load Forecast")
plt.show()

weekday = df[df["Date"].dt.dayofweek < 5]["Usage"].mean()
weekend = df[df["Date"].dt.dayofweek >= 5]["Usage"].mean()

plt.bar(["Weekday","Weekend"], [weekday, weekend])

plt.title("Weekday vs Weekend")
plt.show()