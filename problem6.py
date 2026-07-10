import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

inventory = pd.DataFrame({
    "Day": range(1, 11),
    "SkuID": [101]*10,
    "WarehouseID": [1]*10,
    "CurrentStock": [120,105,90,75,60,45,30,15,-5,25],
    "SafetyStockLevel": [50]*10,
    "DailyReorderQuantity": [20,20,20,20,20,20,20,20,20,20]
})

sales = pd.DataFrame({
    "Day": range(1, 11),
    "ForecastDemand": [12,18,20,25,28,30,35,38,42,22]
})

df = pd.merge(inventory, sales, on="Day", how="inner")

df["Demand_MA_7"] = (
    df["ForecastDemand"]
    .rolling(window=7, min_periods=1)
    .mean()
)

df["Demand_MA_30"] = (
    df["ForecastDemand"]
    .rolling(window=30, min_periods=1)
    .mean()
)

df["StockoutRisk"] = np.where(
    df["CurrentStock"] < df["SafetyStockLevel"],
    True,
    False
)

print("Merged Inventory Data\n")
print(df)


conditions = [
    (df["CurrentStock"] < df["SafetyStockLevel"]) &
    (df["ForecastDemand"] > 30),

    (df["CurrentStock"] < df["SafetyStockLevel"]),

    (df["CurrentStock"] >= df["SafetyStockLevel"])
]

priority = [
    "High",
    "Medium",
    "Low"
]

df["RestockPriority"] = np.select(
    conditions,
    priority,
    default="Low"
)

print("\nRestock Priority\n")
print(df[["CurrentStock","ForecastDemand","RestockPriority"]])


plt.figure(figsize=(10,6))

plt.step(
    df["Day"],
    df["CurrentStock"],
    where="mid",
    linewidth=2,
    label="Current Stock"
)

plt.axhline(
    y=df["SafetyStockLevel"].iloc[0],
    color="green",
    linestyle="--",
    linewidth=2,
    label="Safety Stock"
)

risk = df[df["CurrentStock"] < 0]

plt.scatter(
    risk["Day"],
    risk["CurrentStock"],
    color="red",
    s=100,
    marker="X",
    label="Stock Below Zero"
)

plt.title("Supply Chain Inventory Risk Assessment")
plt.xlabel("Day")
plt.ylabel("Current Stock")
plt.grid(True)
plt.legend()

plt.show()   