from flask import Flask, request, jsonify
import pandas as pd
from google.cloud import storage
import os
import uuid
import requests


os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "liberty-solutions-wealth-66510c5aecc8.json"

# Function to save to Google Cloud Storage
def save_to_cloud_storage(username, email, df):
    unique_id = f"{username}-{email}"
    csv_file = f"{unique_id}.csv"
    df.to_csv(csv_file, index=False)

    storage_client = storage.Client()
    bucket_name = "libertysolutionswiftwealth"  # Replace with your bucket name
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"user_data/linkfilesforeachwm/{csv_file}")
    blob.upload_from_filename(csv_file)
    os.remove(csv_file)
    return f"{bucket_name}/user_data/{username}/{csv_file}"


    

