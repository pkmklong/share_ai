#!/bin/bash

function create_stack() {
    echo "creating aws stack..."
    aws cloudformation create-stack \
    --stack-name $1 \
    --template-body file://$2 \
    --parameters file://$3 \
    --region ${4:- us-west-2}
    }

create_stack
