"""WIP NLP analytics tools - POC to be refactored"""

import streamlit as st
#from chalice import Chalice
#from chalicelib import storage_service
#from chalicelib import transcription_service
#import base64
#import json
#import os
#from os import path
from PIL import Image
from wordcloud import WordCloud, STOPWORDS, ImageColorGenerator
import matplotlib.pyplot as plt
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import nltk
nltk.download('punkt')
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer
import seaborn as sns
import pandas as pd


def wordcloud_viz(text):

      wordcloud = WordCloud().generate(text)
      plt.imshow(wordcloud, interpolation='bilinear')
      plt.axis("off")
      st.pyplot()
      
def sentiment_viz(text):

      text = word_tokenize(text)
      stopWords = set(stopwords.words('english'))
      text = " ".join([w for w in text if w not in stopWords])

      analyser = SentimentIntensityAnalyzer()
      score = analyser.polarity_scores(text)
      st.write(f"{score}")

      df_sent = pd.DataFrame({k:[v] for k, v in score.items()}).T.reset_index() 
      df_sent.columns = ["Sentiment", "Frequency"] 
      plt.figure(figsize=(4,3))
      sns.set(style="white")
      ax = sns.barplot(y="Sentiment", x="Frequency",data=df_sent)
      plt.xlabel('Sentiment')
      plt.ylabel('Frequency')
      plt.title('Polarity')
      st.pyplot()
