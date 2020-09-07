import streamlit as st
from utils import storage_service, transcription_service, nlp_viz
#import base64
import json
import os
from os import path
import pandas as pd

st.set_option('deprecation.showfileUploaderEncoding', False)

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
    
    nlp_viz.wordcloud_viz(transcription_text)
    nlp_viz.sentiment_viz(transcription_text)


filename = st.file_uploader("Choose a file", type=['txt', 'wav', 'mp3', 'mp4'])
if filename is not None:
    file_info = storage_service.upload_file(filename)
    recording_id = file_info["fileId"]

    transcription_text = transcription_service.transcribe_audio(recording_id)
    st.write(transcription_text)
    
    nlp_viz.wordcloud_viz(transcription_text)
    nlp_viz.sentiment_viz(transcription_text)
    
    
text = st.text_input("Free text")
if text:
    nlp_viz.wordcloud_viz(text)
    nlp_viz.sentiment_viz(text)
