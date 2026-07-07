import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Bird": ["Sparrow", "Crow", "Parrot", "Pigeon", "Peacock"],
    "Sightings": [120, 90, 60, 80, 40]
}

df = pd.DataFrame(data)

df = df.sort_values("Sightings", ascending=False)

# Bar Chart
plt.bar(df["Bird"], df["Sightings"])

plt.title("Bird Sightings")
plt.xlabel("Bird Species")
plt.ylabel("Total Sightings")

plt.show()

import pandas as pd
import matplotlib.pyplot as plt


data = {
    "Bird": ["Sparrow", "Crow", "Parrot", "Pigeon", "Peacock"],
    "Sightings": [120, 90, 60, 80, 40]
}

df = pd.DataFrame(data)

df = df.sort_values("Sightings", ascending=False)

# Bar Chart
plt.bar(df["Bird"], df["Sightings"])

plt.title("Bird Sightings")
plt.xlabel("Bird Species")
plt.ylabel("Total Sightings")

plt.show()
