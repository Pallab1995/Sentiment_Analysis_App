import streamlit as st
import pickle
from bs4 import BeautifulSoup
import re
import nltk
from nltk.corpus import stopwords

nltk.download("stopwords")
stop_words = set(stopwords.words("english"))

# Load saved model and vectorizer
model = pickle.load(open("model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

def clean_text(text):
    text = BeautifulSoup(text, "html.parser").get_text()
    text = re.sub(r"[^a-zA-Z ]", "", text)
    text = text.lower()
    text = " ".join([w for w in text.split() if w not in stop_words])
    return text

# Streamlit UI
st.title("📘 Kindle Review Sentiment Analyzer")

review = st.text_area("Enter Review Text Here:")

if st.button("Predict"):
    cleaned_review = clean_text(review)
    vectorized = vectorizer.transform([cleaned_review])
    prediction = model.predict(vectorized.toarray())[0]


    if prediction == 1:
        st.success("Positive Review 👍")
    else:
        st.error("Negative Review 👎")
