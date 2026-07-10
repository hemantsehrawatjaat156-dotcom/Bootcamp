import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "CustomerID":[1,2,3,4,5,6,7,8,9],
    "MonthlyCharges":[500,700,900,1000,1200,1500,1800,2000,5000],
    "TotalCharges":["5000","8000","10000","12000","15000","18000","20000","25000","30000"],
    "Tenure":[2,5,8,12,18,24,30,36,48],
    "ContractType":["Month","Year","Month","Two Year","Year","Month","Two Year","Year","Month"],
    "Churn":["Yes","No","Yes","No","No","Yes","No","Yes","No"]
}

df = pd.DataFrame(data)

df["TotalCharges"] = pd.to_numeric(df["TotalCharges"])

df = pd.get_dummies(df, columns=["ContractType"])

df["Tenure_Group"] = pd.qcut(df["Tenure"], 4)

print("Processed Data")
print(df)


charges = df["MonthlyCharges"].values

Q1 = np.percentile(charges,25)
Q3 = np.percentile(charges,75)

IQR = Q3 - Q1

Lower = Q1 - 1.5*IQR
Upper = Q3 + 1.5*IQR

outliers = charges[(charges<Lower) | (charges>Upper)]

print("\nOutliers:")
print(outliers)


fig, ax = plt.subplots(3,3, figsize=(10,10))

yes = df[df["Churn"]=="Yes"]["MonthlyCharges"]
no = df[df["Churn"]=="No"]["MonthlyCharges"]

ax[0,0].hist(yes, alpha=0.5, label="Yes")
ax[0,0].hist(no, alpha=0.5, label="No")
ax[0,0].set_title("Histogram")
ax[0,0].legend()

ax[0,1].boxplot([yes,no], label=["Yes","No"])
ax[0,1].set_title("Boxplot")

for i in range(3):
    for j in range(3):
        if (i==0 and j<2):
            continue
        ax[i,j].hist(df["MonthlyCharges"])
        ax[i,j].set_title("Plot")

plt.tight_layout()
plt.show()