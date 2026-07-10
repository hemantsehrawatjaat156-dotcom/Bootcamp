import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.DataFrame({
    "ReviewText":[
        " Good Product ",
        "Bad Quality",
        "Excellent Phone",
        "Good Product",
        "Average Item",
        "Very Good Phone"
    ],
    "StarRating":[5,2,5,4,3,5],
    "HelpfulVotes":[20,5,25,15,10,30],
    "PublishDate":pd.date_range("2025-01-01",periods=6)
})


df["ReviewText"] = (
    df["ReviewText"]
    .str.strip()
    .str.lower()
)

df = df[df["ReviewText"].str.contains("good")]

df = df.drop_duplicates(subset="ReviewText")

print(df)


review_length = df["ReviewText"].str.len().to_numpy()

frequency = np.bincount(review_length)

print("\nLength Frequency")
print(frequency)


plt.figure(figsize=(8,5))

scatter = plt.scatter(
    review_length,
    df["HelpfulVotes"],
    c=df["StarRating"],
    cmap="RdYlGn",
    s=100
)

plt.xlabel("Review Length")
plt.ylabel("Helpful Votes")
plt.title("Review Length vs Helpful Votes")

plt.colorbar(scatter,label="Star Rating")

plt.show()