import numpy as np

patients = np.random.randint(50, 251, (30, 5))

print("Patient Data:\n")
print(patients)

mean = np.mean(patients, axis=0)
print("\n1. Department-wise Mean:")
print(mean)

median = np.median(patients, axis=0)
print("\n2. Department-wise Median:")
print(median)

std = np.std(patients, axis=0)
print("\n3. Department-wise Standard Deviation:")
print(std)

highest = np.max(patients, axis=0)
print("\n4. Highest Patient Count in Each Department:")
print(highest)

lowest = np.min(patients, axis=0)
print("\n5. Lowest Patient Count in Each Department:")
print(lowest)

print("\n6. Outliers:")

outlier_mask = np.zeros_like(patients, dtype=bool)

for i in range(5):
    lower = mean[i] - 2 * std[i]
    upper = mean[i] + 2 * std[i]

    print(f"\nDepartment {i+1}:")
    found = False

    for j in range(30):
        if patients[j][i] < lower or patients[j][i] > upper:
            print(f"Day {j+1}: {patients[j][i]}")
            outlier_mask[j][i] = True
            found = True

    if not found:
        print("No Outliers")

new_data = patients.copy()

for i in range(5):
    for j in range(30):
        if outlier_mask[j][i]:
            new_data[j][i] = int(mean[i])

print("\n7. Data After Replacing Outliers:\n")
print(new_data)