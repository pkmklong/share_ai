Skip to content
Search or jump to…

Pull requests
Issues
Marketplace
Explore
 
@pkmklong 
PacktPublishing
/
Hands-On-Artificial-Intelligence-on-Amazon-Web-Services
8
28
Code
Issues
Pull requests
Actions
Wiki
Security
Insights
Hands-On-Artificial-Intelligence-on-Amazon-Web-Services/Chapter04/Capabilities/app.py /
@dineshpackt
dineshpackt Code files updated
Latest commit bc5911a on Oct 8, 2019
 History
 1 contributor
71 lines (54 sloc)  2.18 KB
  
Code navigation is available!
Navigate your code with ease. Click on function and method calls to jump to their definitions or references in the same repository. Learn more

from chalice import Chalice
from chalicelib import storage_service
from chalicelib import transcription_service
from chalicelib import translation_service
from chalicelib import speech_service


import base64
import json

#####
# chalice app configuration
#####
app = Chalice(app_name='Capabilities')
app.debug = True

#####
# services initialization
#####
storage_location = 'aws-bucket-fun'
storage_service = storage_service.StorageService(storage_location)
transcription_service = transcription_service.TranscriptionService(storage_service)


#####
# RESTful endpoints
#####
@app.route('/recordings', methods = ['POST'], cors = True)
def upload_recording():
    """processes file upload and saves file to storage service"""
    request_data = json.loads(app.current_request.raw_body)
    file_name = request_data['filename']
    file_bytes = base64.b64decode(request_data['filebytes'])

    file_info = storage_service.upload_file(file_bytes, file_name)

    return file_info


@app.route('/recordings/{recording_id}/translate-text', methods = ['POST'], cors = True)
def translate_recording(recording_id):
    """transcribes the specified audio then translates the transcription text"""
    request_data = json.loads(app.current_request.raw_body)
    from_lang = request_data['fromLang']
    to_lang = request_data['toLang']

    transcription_text = transcription_service.transcribe_audio(recording_id, from_lang)

    return {
        'text': transcription_text,
    }
