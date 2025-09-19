"""
analysis.py
----------
This script loads the CORD-19 metadata dataset, cleans it,
and generates some exploratory visualizations.
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from wordcloud import WordCloud

# ========== 1. Load Data ==========
print("Loading data...")
df = pd.read_csv("data/metadata.csv")

print("Initial shape:", df.shape)
print(df.info())

# ========== 2. Data Cleaning ==========
# Drop rows with missing essential fields
df = df.dropna(subset=["title", "abstract", "publish_time"])

# Convert publish_time to datetime
df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")

# Extract year
df["year"] = df["publish_time"].dt.year

# Abstract word count
df["abstract_word_count"] = df["abstract"].apply(lambda x: len(str(x).split()))

print("Cleaned shape:", df.shape)

# ========== 3. Analysis & Visualization ==========

# --- Papers per Year ---
papers_per_year = df["year"].value_counts().sort_index()
plt.figure(figsize=(8,5))
sns.barplot(x=papers_per_year.index, y=papers_per_year.values, color="skyblue")
plt.title("Number of Papers per Year")
plt.xlabel("Year")
plt.ylabel("Number of Papers")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("papers_per_year.png")
plt.show()

# --- Top Journals ---
top_journals = df["journal"].value_counts().head(10)
plt.figure(figsize=(8,5))
sns.barplot(y=top_journals.index, x=top_journals.values, palette="viridis")
plt.title("Top Journals Publishing COVID-19 Papers")
plt.xlabel("Number of Papers")
plt.ylabel("Journal")
plt.tight_layout()
plt.savefig("top_journals.png")
plt.show()

# --- Word Cloud of Titles ---
text = " ".join(df["title"].dropna().astype(str).tolist())
wordcloud = WordCloud(width=800, height=400, background_color="white").generate(text)

plt.figure(figsize=(10,6))
plt.imshow(wordcloud, interpolation="bilinear")
plt.axis("off")
plt.title("Word Cloud of Paper Titles")
plt.savefig("wordcloud_titles.png")
plt.show()

print("Analysis complete. Charts saved as PNG images.")
