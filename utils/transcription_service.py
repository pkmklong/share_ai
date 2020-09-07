import boto3
import datetime
import time
import json
from pathlib import Path


class TranscriptionService:
    def __init__(self, storage_service):
        self.client = boto3.client('transcribe')
        self.bucket_name = storage_service.get_storage_location()
        self.storage_service = storage_service

    def transcribe_audio(self, file_name):
        POLL_DELAY = 5

        job_name = file_name + '-trans-' + datetime.datetime.now().strftime("%Y%m%d%H%M%S")
        media_type = Path(file_name).suffix[1:]

        response = self.client.start_transcription_job(
            TranscriptionJobName = job_name,
            LanguageCode = "en-US",
            MediaFormat = media_type,
            Media = {
                'MediaFileUri': "http://" + self.bucket_name + ".s3.amazonaws.com/" + file_name
            },
            OutputBucketName = self.bucket_name
        )

        transcription_job = {
            'jobName': response['TranscriptionJob']['TranscriptionJobName'],
            'jobStatus': 'IN_PROGRESS'
        }

        while transcription_job['jobStatus'] == 'IN_PROGRESS':
            time.sleep(POLL_DELAY)
            response = self.client.get_transcription_job(
                TranscriptionJobName = transcription_job['jobName']
            )
            transcription_job['jobStatus'] = response['TranscriptionJob']['TranscriptionJobStatus']

        transcription_output = self.storage_service.get_file(job_name + '.json')
        return self.extract_transcript(transcription_output)

    @staticmethod
    def extract_transcript(transcription_output):
        transcription = json.loads(transcription_output)
        if transcription['status'] != 'COMPLETED':
            return 'Transcription not available.'

        transcript = transcription['results']['transcripts'][0]['transcript']
        return transcript

