#!/bin/bash

function transcribe() {
    aws transcribe \
    start-transcription-job \
    --transcription-job-name test \
    --language-code en-US \
    --media-format $1 \
    --media MediaFileUri=https://s3.amazon.com/aws-bucket-fun/$2.$1 \
    --output-bucket-name aws-bucket-fun
    }

transcribe
