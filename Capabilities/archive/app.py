from chalice import Chalice
from chalicelib import storage_service
from chalicelib import transcription_service
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
