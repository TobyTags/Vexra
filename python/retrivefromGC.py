from google.cloud import storage
import os
import pandas as pd
import requests

# Configure your Google Cloud credentials
from flask import Flask, request, jsonify
import pandas as pd
from google.cloud import storage
import os
import uuid
import requests
from encryption import decrypt_file

# Configure your Google Cloud credentials
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "liberty-solutions-wealth-66510c5aecc8.json"

def retrieve_data(username, email):
    def download_blob(bucket_name, source_blob_name, destination_file_name):
        """Downloads a blob from the bucket."""
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(source_blob_name)
        blob.download_to_filename(destination_file_name)

        print(f"Downloaded storage object '{source_blob_name}' from bucket '{bucket_name}' to local file '{destination_file_name}'.")

    def read_csv_from_storage(bucket_name, blob_name, local_file_path):
        """Downloads a CSV file from Google Cloud Storage and reads it into a DataFrame."""
        # Download the CSV file from Cloud Storage
        download_blob(bucket_name, blob_name, local_file_path)

        # Decrypt the file
        decrypted_file_path = decrypt_file(local_file_path)

        # Try different encodings
        encodings = ['utf-8', 'ISO-8859-1', 'latin1', 'cp1252']
        df = None

        for encoding in encodings:
            try:
                df = pd.read_csv(decrypted_file_path, encoding=encoding)
                print(f"Successfully read the file with encoding: {encoding}")
                break
            except UnicodeDecodeError:
                print(f"Failed to read the file with encoding: {encoding}")

        if df is None:
            raise ValueError("Failed to read the CSV file with all attempted encodings.")

        # Remove the local file after reading
        if os.path.exists(decrypted_file_path):
            os.remove(decrypted_file_path)

        return df
    
    

    # Construct the blob name based on the username
    bucket_name = "libertysolutionswiftwealth"  # bucket name
    key = f"{username}-{email}"
    blob_name = f"user_data/{key}.enc"
    local_file_path = f"{key}.enc"

    # Read the CSV file into a DataFrame
    df = read_csv_from_storage(bucket_name, blob_name, local_file_path)

    # Remove the local file after reading
    if os.path.exists(local_file_path):
        os.remove(local_file_path)

    return df



