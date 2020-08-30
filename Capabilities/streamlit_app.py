import streamlit as st
from chalice import Chalice
from chalicelib import storage_service
from chalicelib import transcription_service
import base64
import json
import os
from os import path
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


#####
# chalice app configuration
#####

#####
# services initialization
#####
storage_location = 'aws-bucket-fun'
storage_service = storage_service.StorageService(storage_location)
transcription_service = transcription_service.TranscriptionService(storage_service)


"""
#  Welcome to Reflect :) 
"""


filename = st.text_input('Enter a file path:')
if filename:
    file_info = storage_service.upload_file(filename)
    recording_id = file_info["fileId"]

    transcription_text = transcription_service.transcribe_audio(recording_id)
    st.write(transcription_text)

    wordcloud = WordCloud().generate(transcription_text)
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot()

    text = word_tokenize(transcription_text)
    stopWords = set(stopwords.words('english'))
    text = " ".join([w for w in text if w not in stopWords])
    #ps = PorterStemmer()
    
    analyser = SentimentIntensityAnalyzer()
    score = analyser.polarity_scores(text)
    st.write(f"{score}")
           
    df_sent = pd.DataFrame({k:[v] for k, v in score.items()}) 
    plt.figure(figsize=(8,6))
    ax = sns.regplot(x="negative", y="positive",fit_reg=False, scatter_kws={'alpha':0.5},data=df_sent)
    plt.ylabel('Positive Frequency')
    plt.xlabel('Negative Frequency')
    plt.title('Negative Frequency vs Positive Frequency')
    st.pyplot()

    
    
text = st.text_input("for wordcloud")
if text:
    wordcloud = WordCloud().generate(text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot()
    
    
sentence = st.text_input('Write here:') 
if sentence:
    file_bytes = bytes(sentence, 'utf-8')
    file_info = storage_service.upload_file(file_bytes, sentence)
   
text = st.text_input("for wordcloud")
if text:
    wordcloud = WordCloud().generate(text)

    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    st.pyplot()


