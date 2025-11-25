📘 Sentiment Analysis of Kindle Reviews (ML + Streamlit App)


🔗 Live Demo: https://sentimentanalysisapp-mepehnpjfdcgpnlnmjptp3.streamlit.app/

📂 GitHub Repo: https://github.com/Pallab1995/Sentiment_Analysis_App.git

⭐ Project Overview

This project is an end-to-end Sentiment Analysis system built using:

Python

TF-IDF Vectorization

Logistic Regression

NLTK preprocessing

BeautifulSoup text cleaning

Streamlit for Web UI

The model learns from Amazon Kindle product reviews and predicts whether a review is Positive or Negative.
The app is deployed on Streamlit Cloud and accessible with a public URL — perfect for recruiters and portfolio display.

🎯 Features

✔ Cleaned + preprocessed text
✔ TF-IDF vectorization
✔ Logistic Regression classifier
✔ Beautiful Streamlit UI
✔ Real-time prediction
✔ Easy deployment on Streamlit Cloud
✔ Works with any custom user input

🧠 Machine Learning Workflow

Load & explore dataset

Clean text using BeautifulSoup

Remove stopwords (but keep “not”, “no”, “never”)

Convert review text → TF-IDF vectors

Train Logistic Regression model

Evaluate accuracy and classification report

Save model & vectorizer (.pkl)

Build Streamlit interface for live prediction

🧹 Text Preprocessing Includes

Removing HTML tags

Lowercasing

Removing special characters

Stopword removal

Keeping key sentiment words: not, no, never

TF-IDF vectorization

🚀 Technologies Used
Category	Tech
Programming	Python
ML / NLP	Scikit-learn, TF-IDF, Logistic Regression
Text Cleaning	BeautifulSoup, NLTK
Deployment	Streamlit Cloud
Model Files	Pickle (.pkl)
🖥️ Streamlit App Preview

(Upload your UI screenshot here)
Example:

📘 Kindle Review Sentiment Analyzer
-----------------------------------
[ Enter review text here... ]
[ Predict ]

📁 Project Structure
Sentiment_Analysis_App/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── runtime.txt
├── .streamlit/
│     ├── config.toml
│     └── theme.toml
│
└── Data/
      └── all_kindle_review.csv

▶️ How to Run Locally
1️⃣ Install dependencies
pip install -r requirements.txt

2️⃣ Run Streamlit
streamlit run app.py


Open browser → http://localhost:8501

🌐 How to Deploy (Streamlit Cloud)

Push project to GitHub

Open https://share.streamlit.io

Click New App

Select:

Repo: Sentiment_Analysis_App

Branch: main

File: app.py

Click Deploy

🔍 Example Predictions
Review Text	Prediction
“Loved this book! Very useful.”	👍 Positive
“Waste of money. Bad writing.”	👎 Negative

🤝 Author

Pallab Sharma

Data Analyst → AI/ML Practitioner

🔗 GitHub Profile(https://github.com/Pallab1995)

📧 Email: pallabsharma100@gmail.com
