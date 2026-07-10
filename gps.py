import pandas as pd
import numpy as np

data = {
    "VehicleID":[101,101,101,102,102],
    "Timestamp":[
        "2025-01-01 08:00",
        "2025-01-01 08:05",
        "2025-01-01 08:10",
        "2025-01-01 08:00",
        "2025-01-01 08:05"
    ],
    "Latitude":[28.61,28.62,28.63,28.60,28.61],
    "Longitude":[77.20,77.21,77.22,77.19,77.20],
    "Speed":[10,20,15,35,45]
}

df = pd.DataFrame(data)

df["Prev_Lat"] = df["Latitude"].shift()
df["Prev_Lon"] = df["Longitude"].shift()

R = 6371

def haversine(lat1, lon1, lat2, lon2):
    if pd.isna(lat2):
        return np.nan

    lat1, lon1, lat2, lon2 = map(np.radians,[lat1,lon1,lat2,lon2])

    dlat = lat2-lat1
    dlon = lon2-lon1

    a = np.sin(dlat/2)**2 + np.cos(lat1)*np.cos(lat2)*np.sin(dlon/2)**2
    c = 2*np.arcsin(np.sqrt(a))
    return R*c

df["Distance(km)"] = df.apply(lambda x:
    haversine(x["Prev_Lat"],x["Prev_Lon"],
              x["Latitude"],x["Longitude"]),axis=1)

df["Lat_Grid"] = df["Latitude"].round(1)
df["Lon_Grid"] = df["Longitude"].round(1)

group = df.groupby(["Lat_Grid","Lon_Grid"])["Speed"].mean()

print(df)
print("\nAverage Speed by Grid")
print(group)