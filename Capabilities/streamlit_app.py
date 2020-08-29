import streamlit as st
from chalice import Chalice
from chalicelib import storage_service
from chalicelib import transcription_service
import base64
import json

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
#  Welcome to Reflect!
"""
