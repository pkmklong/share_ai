"""WIP NLP analytics tools - POC to be refactored"""

import streamlit as st
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk

nltk.download("punkt")
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import seaborn as sns
import pandas as pd
from typing import List


def wordcloud_viz(text: str) -> plt.Figure:
    """Create visual of wordclould"""

    wordcloud = WordCloud().generate(text)
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.axis("off")
    st.pyplot()


def tokenize(text: str) -> str:
    """Token and remove stop words"""

    text = word_tokenize(text)
    stopWords = set(stopwords.words("english"))
    text = " ".join([w for w in text if w not in stopWords])
    return text


def sentiment_viz(text: str) -> plt.Figure:
    """Create visual of sentiment analysis"""

    text = tokenize(text)

    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(text)
    st.write(f"{score}")

    df_sent = pd.DataFrame({k: [v] for k, v in score.items()}).T.reset_index()
    df_sent.columns = ["Sentiment", "Frequency"]
    plt.figure(figsize=(4, 3))
    sns.set(style="white")
    ax = sns.barplot(y="Sentiment", x="Frequency", data=df_sent)
    plt.xlabel("Sentiment")
    plt.ylabel("Frequency")
    plt.title("Polarity")
    st.pyplot()
