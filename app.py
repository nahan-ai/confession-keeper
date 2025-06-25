import streamlit as st
from textblob import TextBlob
import matplotlib.pyplot as plt
import random

# --- Style for button and background ---
st.markdown("""
<style>
/* Button style */
div.stButton > button:first-child {
    background-color: #ff6347;  /* tomato red */
    color: white;
    border-radius: 12px;
    height: 3em;
    width: 100%;
    font-size: 20px;
    font-weight: bold;
    transition: background-color 0.3s ease;
}
div.stButton > button:first-child:hover {
    background-color: #e5533c;  /* darker red on hover */
    color: #fff;
}
/* Background gradient */
body {
    background: linear-gradient(135deg, #fff5e1, #ffd6ba);
    color: #333333;
    font-family: 'Poppins', sans-serif;
}
/* Confession box */
.confession-box {
    background:#fff;
    padding:15px;
    border-radius:12px;
    box-shadow: 0 0 10px rgba(0,0,0,0.1);
    margin-bottom: 15px;
    font-size: 16px;
}
</style>
""", unsafe_allow_html=True)

# --- Initialize session state ---
if 'confessions' not in st.session_state:
    st.session_state.confessions = []

# --- Quotes with emojis ---
quotes = [
    "🌟 Every cloud has a silver lining.",
    "💡 Speak your mind, even if your voice shakes.",
    "💖 Healing begins when you open up.",
    "✨ Your feelings are valid.",
    "🌈 This too shall pass.",
    "🔥 Be fearless in the pursuit of what sets your soul on fire.",
    "🌸 You are stronger than you think."
]

# --- Sentiment analysis function ---
def analyze_sentiment(text):
    blob = TextBlob(text)
    polarity = blob.sentiment.polarity
    if polarity > 0.1:
        return "Positive", "😄✨"
    elif polarity < -0.1:
        return "Negative", "😞💔"
    else:
        return "Neutral", "😐🤔"

# --- Page setup ---
st.set_page_config(page_title="Confession Keeper", page_icon="🕊️", layout="centered")

# --- Title and intro ---
st.title("🕊️ The Confession Keeper")
st.write("Write your secret confession below. Your feelings matter! 💬")
st.info(random.choice(quotes))

# --- Layout: two columns ---
col1, col2 = st.columns([3,1])

with col1:
    confession = st.text_area("Your confession 📝:", height=150)
    if st.button("Submit 💌"):
        if confession.strip() == "":
            st.error("Please write something before submitting.")
        else:
            sentiment, emoji = analyze_sentiment(confession)
            st.session_state.confessions.append((confession, sentiment))
            st.success(f"Saved! Sentiment detected: {sentiment} {emoji}")
            st.balloons()

with col2:
    if st.session_state.confessions:
        st.subheader("Sentiment Counts 📊")
        sentiments = [s for _, s in st.session_state.confessions]
        counts = {
            "Positive": sentiments.count("Positive"),
            "Neutral": sentiments.count("Neutral"),
            "Negative": sentiments.count("Negative")
        }
        fig, ax = plt.subplots()
        ax.bar(counts.keys(), counts.values(), color=['#4caf50', '#ffc107', '#f44336'])
        ax.set_title("Sentiment Counts")
        ax.set_ylabel("Number of Confessions")
        st.pyplot(fig)

# --- Show last 5 confessions with styling ---
if st.session_state.confessions:
    st.subheader("Past Confessions and their Moods")
    for c, s in st.session_state.confessions[-5:][::-1]:
        emoji = "😊" if s == "Positive" else "😔" if s == "Negative" else "😐"
        st.markdown(f'''
            <div class="confession-box">
                {c}<br><b>Mood:</b> {s} {emoji}
            </div>
        ''', unsafe_allow_html=True)
