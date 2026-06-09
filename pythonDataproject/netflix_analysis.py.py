# Netflix Data Analysis using Python

import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter



# 1. Load Dataset  -------------------------------------


df = pd.read_csv("netflix_titles_nov_2019.csv")



# 2. Basic Dataset Information -------------------------------



print("Dataset Shape:", df.shape)
print("\nColumns:")
print(df.columns)

print("\nMissing Values:")
print(df.isnull().sum())



# 3. Data Cleaning --------------------------------



df["director"] = df["director"].fillna("Unknown")
df["cast"] = df["cast"].fillna("Missing")
df["date_added"] = df["date_added"].fillna("Missing")
df["rating"] = df["rating"].fillna("Not Available")
df["country"] = df["country"].fillna("Unknown")


# 4. Movies vs TV Shows -----------------------



df["type"].value_counts().plot(
kind="bar",
color=["blue", "green"],
edgecolor="black"
)

plt.title("Movies vs TV Shows on Netflix")
plt.xlabel("Content Type")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()



# 5. Top 10 Countries  --------------------



df["country"].value_counts().head(10).plot(
kind="barh",
edgecolor="black"
)

plt.title("Top 10 Countries on Netflix")
plt.xlabel("Number of Titles")
plt.ylabel("Country")
plt.gca().invert_yaxis()
plt.show()



# 6. Top 5 Ratings  ------------------



df["rating"].value_counts().head(5).plot(
kind="bar",
edgecolor="black"
)

plt.title("Top 5 Netflix Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")
plt.xticks(rotation=0)
plt.show()


# 7. Top Genres ------------------


all_genres = []

for genre in df["listed_in"]:
   genres = genre.split(",")
   all_genres.extend(genres)

top_genres = Counter(all_genres).most_common(10)

genres = [item[0].strip() for item in top_genres]
counts = [item[1] for item in top_genres]

plt.barh(genres, counts)
plt.gca().invert_yaxis()
plt.title("Top 10 Genres on Netflix")
plt.xlabel("Count")
plt.ylabel("Genre")
plt.show()


# 8. Release Year Trend --------------------



year_count = df["release_year"].value_counts().sort_index()

plt.plot(year_count.index, year_count.values)

plt.title("Netflix Content Growth Over Time")
plt.xlabel("Release Year")
plt.ylabel("Number of Titles")
plt.show()

# Final Insights -----------------------------


"""

1. Netflix contains more Movies than TV Shows.

2. United States contributes the highest amount of content,
   followed by India.

3. TV-MA is the most common rating on Netflix.

4. International Movies is the most common genre.

5. Netflix content increased significantly after 2015.

6. Most content was released around 2017–2018.
   """
