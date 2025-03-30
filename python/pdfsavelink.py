from flask import Flask, request, jsonify
import pandas as pd
from google.cloud import storage
import os
import uuid
import requests




# Configure your Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "liberty-solutions-wealth-66510c5aecc8.json"

def save_to_cloud_storagepdflink(pdf_file_path, username, email, WMusename):
    try:
        # Create a unique ID based on the username and email
        unique_id = f"{username}-{email}"

        # Initialize the Google Cloud Storage client
        storage_client = storage.Client()
        bucket_name = "libertysolutionswiftwealth"  # Replace with your bucket name
        bucket = storage_client.bucket(bucket_name)

        # Create a blob object with a unique path
        blob = bucket.blob(f"forWMconcole/pdf/{WMusename}/{unique_id}.pdf")

        # Upload the PDF file to Google Cloud Storage
        blob.upload_from_filename(pdf_file_path)

        # Optionally remove the local file after upload
        if os.path.exists(pdf_file_path):
            os.remove(pdf_file_path)

        return "SENT PDF"

    except Exception as e:
        print(f"Error saving PDF to Cloud Storage: {e}")
        return "ERROR"
    

