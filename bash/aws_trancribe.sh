#!/bin/bash

function transcribe() {
    aws transcribe \
    start-transcription-job \
    --transcription-job-name test \
    --language-code en-US \
    --media-format mp4 \
    --media MediaFileUri=https://s3.amazon.com/aws-bucket-fun/testing.mp4 \
    --output-bucket-name aws-bucket-fun
    }

transcribe
