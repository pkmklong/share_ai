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
#try:
#    with open(filename) as input:
#        st.text(input.read())
#        text = input.read()
#except FileNotFoundError:
#    st.error('File not found.')  
if filename:
    #file_bytes = bytes(text, 'utf-8')
#     file = open(filename, 'rb')
#     file_bytes = base64.b64decode(file)
    file_info = storage_service.upload_file(Filename = filename)
    
  
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


