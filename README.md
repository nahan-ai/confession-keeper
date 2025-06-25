# 🕊️ The Confession Keeper

An AI-powered web application that allows users to anonymously submit confessions and receive emotional feedback using sentiment analysis.

---

## 📌 Project Overview

**The Confession Keeper** is built using **Python**, **Streamlit**, and **TextBlob**.  
It provides a safe space for users to express their emotions anonymously.  
Each confession is analyzed for sentiment (Positive, Negative, or Neutral), and mood-related emojis and motivational quotes are displayed to uplift the user.

---

## 🔍 Objective

- Build a beautiful AI-powered web app with sentiment analysis
- Enable users to submit anonymous confessions
- Display sentiment using **TextBlob**
- Present results with emojis, quotes, and charts
- Deploy the app using **Streamlit Cloud**

---

## 🌟 Features

- 📝 Anonymous confession submission  
- 💬 Sentiment analysis with emotional emoji feedback  
- 📈 Bar chart of mood trends  
- 🌈 Motivational quotes on each visit  
- 🎨 Beautiful UI with custom fonts and colors

---

## 📊 Sentiment Classification

| Mood Type  | Polarity Range    | Emoji Example |
|------------|-------------------|----------------|
| Positive   | > 0.1             | 😄✨            |
| Neutral    | -0.1 to 0.1       | 😐🤔            |
| Negative   | < -0.1            | 😞💔            |

Sentiment is determined using **TextBlob**, a natural language processing tool in Python.

---

## 💻 Tech Stack

| Tool          | Description                              |
|---------------|------------------------------------------|
| Python        | Programming Language                     |
| Streamlit     | UI Framework for web apps                |
| TextBlob      | Sentiment Analysis Library               |
| Matplotlib    | Visualization (bar chart)                |
| HTML/CSS      | Styling via Streamlit markdown injection |

---

## 📷 Screenshots

> *(Optional – You can upload screenshots to an `/images` folder and replace this image below)*

![App Screenshot](images/screenshot1.png)

---

## 🚀 How to Run Locally

1. **Clone the repository**

```bash
git clone https://github.com/nahan-ai/confession-keeper.git
