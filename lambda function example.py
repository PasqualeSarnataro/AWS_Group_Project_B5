#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import boto3
import os
import tempfile
import pandas as pd
import json

s3 = boto3.client('s3')
sagemaker = boto3.client('sagemaker-runtime')
SOURCE_BUCKET = 'intake-bucket-b5'
DEST_BUCKET = 'prediction-bucket-b5'
SAGEMAKER_ENDPOINT_NAME = 'pasquale-sagemaker-endpoint'

def lambda_handler(event, context):
    # Get the uploaded CSV file details from the S3 event
    record = event['Records'][0]
    bucket = record['s3']['bucket']['name']
    key = record['s3']['object']['key']
    
    # Download the CSV file from S3 to a temporary file
    with tempfile.TemporaryFile() as tmp_file:
        s3.download_fileobj(bucket, key, tmp_file)
        tmp_file.seek(0)

        # Preprocess the data
        input_data = preprocess_data(tmp_file)

        # Get predictions from SageMaker endpoint
        predictions = get_predictions(input_data)

        # Upload the predictions to the destination S3 bucket
        upload_predictions(predictions)

def preprocess_data(file):
    df = pd.read_csv(file)
    # Perform any additional preprocessing steps here
    input_data = df.to_json(orient='split', index=False)
    return input_data

def get_predictions(input_data):
    response = sagemaker.invoke_endpoint(
        EndpointName=SAGEMAKER_ENDPOINT_NAME,
        ContentType='application/json',
        Body=json.dumps({'instances': input_data})
    )
    predictions = json.loads(response['Body'].read().decode('utf-8'))
    return predictions

def upload_predictions(predictions):
    output_data = pd.DataFrame(predictions)
    output_key = 'predictions/result.csv'
    with tempfile.TemporaryFile() as tmp_file:
        output_data.to_csv(tmp_file, index=False)
        tmp_file.seek(0)
        s3.upload_fileobj(tmp_file, DEST_BUCKET, output_key)

