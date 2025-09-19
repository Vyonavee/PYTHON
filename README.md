# Frameworks_Assignment - CORD-19 Data Explorer

## 📌 Overview
This project analyzes the **CORD-19 research dataset** (metadata.csv) and provides:
- Data cleaning & preprocessing
- Visualizations (papers per year, top journals, word cloud of titles)
- An interactive Streamlit web app

## 🛠 Tools Used
- Python 3.7+
- pandas
- matplotlib & seaborn
- wordcloud
- Streamlit

## 📂 Project Structure
Frameworks_Assignment/
│── data/
│ └── metadata.csv
│── analysis.py # Data cleaning + visualizations
│── app.py # Streamlit interactive app
│── requirements.txt # Dependencies
└── README.md # Documentation

## Documentation

## 🚀 How to Run

### 1. Install dependencies
```bash
pip install -r requirements.txt

### 2. Run analysis
python analysis.py

### 3. Run Streamlit app
streamlit run app.py

 Then open the local server URL (e.g. http://localhost:8501) in your browser.

📊 Outputs

Bar chart of papers per year

Top 10 journals publishing COVID-19 research

Word cloud of paper titles

Interactive app for filtering and exploring

