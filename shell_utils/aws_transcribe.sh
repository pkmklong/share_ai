#!/bin/bash

function transcribe() {
    aws transcribe \
    start-transcription-job \
    --transcription-job-name $1 \
    --language-code en-US \
    --media-format wav \
    --media MediaFileUri=https://s3.amazon.com/aws-bucket-fun/ios.wav \
    --output-bucket-name aws-bucket-fun
    }

transcribe $1 $2
