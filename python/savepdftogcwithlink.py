from flask import Flask, request, jsonify
import pandas as pd
from google.cloud import storage
import os
import base64
from cryptography.hazmat.primitives.ciphers import Cipher, algorithms, modes
from cryptography.hazmat.backends import default_backend

from encryption import encrypt_file

# Configure your Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "liberty-solutions-wealth-66510c5aecc8.json"


# Function to save to Google Cloud Storage
def save_to_cloud_storagelink(username, email, df, WMusename):
    print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
    unique_id = f"{username}-{email}"

    csv_file = f"{unique_id}.enc"

    # Save the DataFrame to a CSV file in the top-level directory
    df.to_csv(csv_file, index=False)

    encrypt_file(csv_file)

    print("!!!!!!!!!!!!!!!")
    print(WMusename)
    print(csv_file)
    print("!!!!!!!!!!!!!!!")

    storage_client = storage.Client()
    bucket_name = "libertysolutionswiftwealth"  # Replace with your bucket name
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(f"forWMconcole/pdfforreal/linkfilesforeachwm/{WMusename}/{csv_file}")
    blob.upload_from_filename(csv_file)
    os.remove(csv_file)
    return f"{bucket_name}/user_data/{username}/{csv_file}"