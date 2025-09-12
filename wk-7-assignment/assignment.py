# assignment.py
"""
Assignment: Analyzing Data with Pandas and Visualizing Results with Matplotlib

This script demonstrates:
- Loading and exploring a dataset
- Performing basic data analysis
- Creating different types of visualizations
"""

import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_iris

# ------------------------
# Task 1: Load and Explore
# ------------------------

try:
    # Load Iris dataset from sklearn
    iris = load_iris(as_frame=True)
    df = iris.frame  # Convert to pandas DataFrame

    print("✅ Dataset loaded successfully!\n")
except FileNotFoundError:
    print("❌ Error: File not found.")
    exit()
except Exception as e:
    print(f"❌ Unexpected error: {e}")
    exit()

# Display first few rows
print("First 5 rows of dataset:")
print(df.head(), "\n")

# Check structure
print("Dataset Info:")
print(df.info(), "\n")

# Check missing values
print("Missing values per column:")
print(df.isnull().sum(), "\n")

# Clean data (Iris has no missing values, but let's show how we’d handle it)
df = df.dropna()

# ------------------------
# Task 2: Basic Analysis
# ------------------------

print("Basic statistics of numerical columns:")
print(df.describe(), "\n")

# Grouping by species and computing mean
group_means = df.groupby("target").mean()
print("Mean values grouped by species (0=setosa, 1=versicolor, 2=virginica):")
print(group_means, "\n")

# Observation example
print("Observation: Virginica tends to have the largest petal length and width.\n")

# ------------------------
# Task 3: Visualizations
# ------------------------

# 1. Line chart (showing sepal length for first 30 samples)
plt.figure(figsize=(8,5))
plt.plot(df["sepal length (cm)"][:30], marker='o')
plt.title("Line Chart - Sepal Length (first 30 samples)")
plt.xlabel("Sample Index")
plt.ylabel("Sepal Length (cm)")
plt.grid(True)
plt.show()

# 2. Bar chart (average petal length per species)
plt.figure(figsize=(8,5))
group_means["petal length (cm)"].plot(kind="bar", color=["skyblue","lightgreen","salmon"])
plt.title("Bar Chart - Average Petal Length per Species")
plt.xlabel("Species (0=setosa, 1=versicolor, 2=virginica)")
plt.ylabel("Petal Length (cm)")
plt.show()

# 3. Histogram (distribution of sepal width)
plt.figure(figsize=(8,5))
plt.hist(df["sepal width (cm)"], bins=15, color="purple", edgecolor="black")
plt.title("Histogram - Distribution of Sepal Width")
plt.xlabel("Sepal Width (cm)")
plt.ylabel("Frequency")
plt.show()

# 4. Scatter plot (sepal length vs petal length)
plt.figure(figsize=(8,5))
plt.scatter(df["sepal length (cm)"], df["petal length (cm)"], c=df["target"], cmap="viridis", alpha=0.7)
plt.title("Scatter Plot - Sepal Length vs Petal Length")
plt.xlabel("Sepal Length (cm)")
plt.ylabel("Petal Length (cm)")
plt.colorbar(label="Species")
plt.show()

print("✅ All tasks completed successfully!")
