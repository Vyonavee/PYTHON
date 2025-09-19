"""
app.py
------
Streamlit web application for interactive exploration of CORD-19 dataset.
Run with: streamlit run app.py
"""

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ========== 1. Load Data ==========
@st.cache_data
def load_data():
    df = pd.read_csv("data/metadata.csv")
    df = df.dropna(subset=["title", "abstract", "publish_time"])
    df["publish_time"] = pd.to_datetime(df["publish_time"], errors="coerce")
    df["year"] = df["publish_time"].dt.year
    df["abstract_word_count"] = df["abstract"].apply(lambda x: len(str(x).split()))
    return df

df = load_data()

# ========== 2. App Layout ==========
st.title("CORD-19 Data Explorer")
st.write("Simple exploration of COVID-19 research papers (metadata only).")

# Year range filter
min_year, max_year = int(df["year"].min()), int(df["year"].max())
years = st.slider("Select year range", min_year, max_year, (2020, 2021))
filtered = df[(df["year"] >= years[0]) & (df["year"] <= years[1])]

# --- Papers per Year ---
st.subheader("Number of Papers per Year")
papers_per_year = filtered["year"].value_counts().sort_index()
st.bar_chart(papers_per_year)

# --- Top Journals ---
st.subheader("Top Journals")
top_journals = filtered["journal"].value_counts().head(10)
fig, ax = plt.subplots()
sns.barplot(y=top_journals.index, x=top_journals.values, palette="mako", ax=ax)
ax.set_title("Top Journals Publishing Papers")
ax.set_xlabel("Number of Papers")
ax.set_ylabel("Journal")
st.pyplot(fig)

# --- Show Sample Data ---
st.subheader("Sample of Data")
st.dataframe(filtered[["title", "authors", "journal", "year"]].head(10))
