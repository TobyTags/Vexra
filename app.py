from flask import Flask, render_template, request, jsonify, session, redirect, make_response, Response
import pandas as pd
import sys
import os

# Ensure the `python` folder is in sys.path
sys.path.append(os.path.abspath("python"))

from python.pdf_report import make_and_save_pdf
from python.send_email import email
from python.calculations import calculations

from flask import Flask, render_template, request, send_file, url_for
import pandas as pd

from python.send_email import email
from python.calculations import calculations

import json

from python.savetoGC import save_to_cloud_storage
import requests

from python.retrivefromGC import retrieve_data

from python.pdfsavegc import save_to_cloud_storagepdf

import logging

from flask import Flask, request, jsonify
from google.cloud import storage
from google.auth.transport.requests import Request
from datetime import datetime, timedelta
import os

from python.savepdftogcwithlink import save_to_cloud_storagelink
from python.pdfsavelink import save_to_cloud_storagepdflink

from python.retriveCSVfromgc import retrieve_dataforfetchnew

from cryptography.fernet import Fernet

from python.encryption import encrypt_data
from python.encryption import decrypt_data




app = Flask(__name__)

app.secret_key = 'supersecretkey'  # Necessary for using sessions

@app.route('/makelink', methods=['POST'])
def makelink():
    try:
        CLusername = request.form['name']
        CLemail = request.form['email']

        data = request.form.to_dict()
        WMusename = data.get('username')

        # Correct the URL to use /questionairlink
        survey_url = url_for('questionairlink', CLname=CLusername, CLemail=CLemail, WMusename=WMusename, _external=True)

        return jsonify({'survey_url': survey_url})
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    


@app.route('/makelinkpage')
def makelinkpage():
    return render_template('makelink.html')


def main(raw_df, username, email):
   
    # Perform calculations
    clean_df = calculations(raw_df)

    print(clean_df)

    make_and_save_pdf(clean_df)

    pdf_file_path = "OUTPUT5.pdf"
    
    save_to_cloud_storagepdf(pdf_file_path, username, email)

    # Send an email
    # email()

    return ("ALL GOOD")




@app.route('/')
def index():
    response = make_response(render_template('124757/site/index.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/logout')
def logout():
    return render_template('124757/site/index.html')

@app.route('/signup')
def Sign_Up():
    return render_template('signupform.html')

@app.route('/logedin')
def LogedIn():
    response = make_response(render_template('LogedInDashboard.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response

@app.route('/financial_personality')
def financial_personality():
    return render_template('financial_personality.html')

@app.route('/gotomakenewac')
def gotomakenewac():
    return render_template('signupforcreatenewac.html')

@app.route('/thankyoug')
def thankyoug():
    return render_template('thankyoug.html')

@app.route('/questionair')
def questionair():
    return render_template('servery.html')


@app.route('/questionairlink')
def questionairlink():
    return render_template('surveylink.html')

@app.route('/privacystatment')
def privacystatment():
    return render_template('privacystatment.html')


@app.route('/submit', methods=['POST'])
def submit():
    try:

        print("Received a submit request")

        # Get JSON data from the request
        data = request.get_json()
        print(f"Received data: {data}")

        # Extract username from data
        username = data.get('username')
        if not username:
            return jsonify({'status': 'error', 'message': 'Username not provided in data'}), 400
        
        email = data.get('email')
        if not email:
            return jsonify({'status': 'error', 'message': 'Username not provided in data'}), 400

        # Check if data is empty or invalid
        if not data:
            raise ValueError("No data provided or data is invalid")

        # Remove username from data to avoid storing it in DataFrame
        del data['username']
        del data['email']

        # Convert the data to a Pandas DataFrame
        dfrawT = pd.DataFrame([data])
        print(f"Converted data to DataFrame: {dfrawT}")

        #saving file to GC sorage
        save_to_cloud_storage(username, email, dfrawT)


        #Actual report output is being made here, dont mess with these lines -----------
        newdf = calculations(dfrawT)

        make_and_save_pdf(newdf)

        pdf_file_path = "OUTPUT5.pdf"
        save_to_cloud_storagepdf(pdf_file_path, username, email)

        print("------------------------------------------------------")


        # Return a success response
        return jsonify({'status': 'success', 'data': data})

    except Exception as e:
        # Print the error and send an error response
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500



    


@app.route('/showoutput', methods=['POST'])
def showoutput():

    print(1)

    # Get JSON data from the request
    data = request.get_json()
    print(f"Received data: {data}")

    # Extract username from data
    username = data.get('username')
    if not username:
        return jsonify({'status': 'error', 'message': 'Username not provided in data'}), 400
    
    email = data.get('email')
    if not email:
        return jsonify({'status': 'error', 'message': 'Username not provided in data'}), 400

    # Check if data is empty or invalid
    if not data:
        raise ValueError("No data provided or data is invalid")

    print(2)
    # Remove username from data to avoid storing it in DataFrame
    del data['username']
    del data['email']

    print(f"{username}, {email} this is username and email toby t")
    print(3)


    try:
        unique_id = f"{username}-{email}"
        bucket_name = "libertysolutionswiftwealth"  # Replace with your bucket name
        blob_path = f"user_data/pdfreports/{unique_id}.pdf"
        
        # Initialize a Google Cloud Storage client
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blob = bucket.blob(blob_path)

        if not blob.exists():
            return jsonify({'status': 'error', 'message': 'PDF file does not exist'}), 404
        
        # Generate a signed URL
        expiration = datetime.utcnow() + timedelta(minutes=15)  # URL valid for 15 minutes
        signed_url = blob.generate_signed_url(
            expiration=expiration,
            method='GET'
        )

        return jsonify({'status': 'success', 'pdf_url': signed_url})
    
    except Exception as e:
        print(f"Error getting signed URL: {e}")
        return None





# old pdf pulling all to dashboard code
@app.route('/showoutputtakeall', methods=['POST'])
def showoutputtakeall():
    try:
        # Get JSON data from the request
        data = request.get_json()
        if not data:
            logging.error("No data provided or data is invalid")
            return jsonify({'status': 'error', 'message': 'No data provided or data is invalid'}), 400

        # Extract username and email from data
        WMusername = data.get('WMusername')

        if not WMusername:
            logging.error("Username and email are required")
            return jsonify({'status': 'error', 'message': 'Username and email are required'}), 400

        bucket_name = "libertysolutionswiftwealth"
        blob_path = f"forWMconcole/pdf/{WMusername}/"

        # Initialize a Google Cloud Storage client
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)

        # List all blobs (files) in the specified directory
        blobs = bucket.list_blobs(prefix=blob_path)
        
        pdf_urls = []
        expiration = datetime.utcnow() + timedelta(minutes=15)

        for blob in blobs:
            logging.info(f"Processing blob: {blob.name}")
            if blob.name.endswith('.pdf'):
                signed_url = blob.generate_signed_url(
                    expiration=expiration,
                    method='GET'
                )
                pdf_urls.append({
                    'file_name': blob.name,
                    'pdf_url': signed_url
                })

        if not pdf_urls:
            logging.info("No PDF files found")
            return jsonify({'status': 'error', 'message': 'No PDF files found'}), 404

        logging.info(f"Returning {len(pdf_urls)} PDF URLs")
        return jsonify({'status': 'success', 'pdf_urls': pdf_urls})

    except Exception as e:
        logging.error(f"Exception occurred: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500







import csv
from io import StringIO

from flask import Flask, request, jsonify
from google.cloud import storage
from datetime import datetime, timedelta
import logging

@app.route('/htmlpull', methods=['POST'])
def htmlpull():
    print("Entering /htmlpull route")
    try:
        # Attempt to get JSON data from the request
        data = request.get_json()
        print("Data received:", data)

        if not data:
            print("No data provided or data is invalid")
            logging.error("No data provided or data is invalid")
            return jsonify({'status': 'error', 'message': 'No data provided or data is invalid'}), 400

        WMusername = data.get('WMusername')
        print("WMusername extracted:", WMusername)

        if not WMusername:
            print("Username is required")
            logging.error("Username is required")
            return jsonify({'status': 'error', 'message': 'Username is required'}), 400

        bucket_name = "libertysolutionswiftwealth"
        blob_path = f"forWMconcole/pdfforreal/linkfilesforeachwm/{WMusername}/"

        print("Bucket name:", bucket_name)
        print("Blob path:", blob_path)

        # Initialize Google Cloud Storage client and get the bucket
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=blob_path)

        print("Blobs listed")

        file_names = []

        for blob in blobs:
            # Extract the file name from the blob path
            file_name_with_extension = blob.name.split('/')[-1]  # Get the last part after the last '/'
            print("File name with extension:", file_name_with_extension)

            if file_name_with_extension.endswith('.enc'):
                # Remove the `.csv` extension
                file_name = file_name_with_extension.replace('.enc', '')
                print("File name without extension:", file_name)
                file_names.append({
                    'file_name': file_name
                })

        if not file_names:
            print("No CSV files found")
            return jsonify({'status': 'success', 'file_names': []})  # Ensure file_names is always present

        print(f"Returning {len(file_names)} file names")
        return jsonify({'status': 'success', 'file_names': file_names})

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


# KmHILCCP7A%3D%3D
# CUPQPjaZ5Aef1A==
















@app.route('/run', methods=['POST'])
def run():
    # Run the main function
    main()

    return render_template('LogedInDashboard.html', pdf_generated=True)









@app.route('/submitlink', methods=['POST'])
def submitlink():
    try:

        print("Received a submit request")

        # Get JSON data from the request
        data = request.get_json()
        print(f"Received data: {data}")

        # Extract username from data
        CLusername = data.get('CLusername')
        if not CLusername:
            return jsonify({'status': 'error', 'message': 'Username not provided in data'}), 400
        
        CLemail = data.get('CLemail')
        if not CLemail:
            return jsonify({'status': 'error', 'message': 'Username not provided in data'}), 400

        WMusename = data.get('WMusename')
        if not WMusename:
            return jsonify({'status': 'error', 'message': 'Username not provided in data'}), 400

        # Check if data is empty or invalid
        if not data:
            raise ValueError("No data provided or data is invalid")

        # Remove username from data to avoid storing it in DataFrame
        del data['CLemail']
        del data['WMusename']

        # Convert the data to a Pandas DataFrame
        dfrawT = pd.DataFrame([data])
        print(f"Converted data to DataFrame: {dfrawT}")


        print(1)
        #saving file to GC sorage
        save_to_cloud_storagelink(CLusername, CLemail, dfrawT, WMusename)
        print(1)
        
        # Save the DataFrame to a CSV file
        #csv_file = "toby.csv"
        #dfrawT.to_csv(csv_file, index=False)
        #print(f"Data saved to {csv_file}")


        newdf = calculations(dfrawT)

        make_and_save_pdf(newdf)

        pdf_file_path = "OUTPUT5.pdf"
        save_to_cloud_storagepdflink(pdf_file_path, CLusername, CLemail, WMusename)

        print("!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        # Return a success response
        return jsonify({'status': 'success', 'data': data})


    except Exception as e:
        # Print the error and send an error response
        print(f"Error: {e}")
        return jsonify({'status': 'error', 'message': str(e)}), 500



import firebase_admin
from firebase_admin import credentials

import os
from dotenv import load_dotenv

# Load environment variables from keys.env file
load_dotenv('keys.env')

#load once and keep it loaded
cred = credentials.Certificate("vexra-f034a-firebase-adminsdk-4czli-c1c64c008d.json")
firebase_admin.initialize_app(cred)


@app.route('/firebase-config')
def firebase_config():
    config = {
        "apiKey": os.getenv("FIREBASE_API_KEY"),
        "authDomain": os.getenv("FIREBASE_AUTH_DOMAIN"),
        "projectId": os.getenv("FIREBASE_PROJECT_ID"),
        "storageBucket": os.getenv("FIREBASE_STORAGE_BUCKET"),
        "messagingSenderId": os.getenv("FIREBASE_MESSAGING_SENDER_ID"),
        "appId": os.getenv("FIREBASE_APP_ID"),
        "measurementId": os.getenv("FIREBASE_MEASUREMENT_ID")
    }
    return jsonify(config)





    



@app.route('/michlereportmaking', methods=['POST'])
def michlereportmaking():
    try:
        data = request.get_json()
        print(f"Received data: {data}")

        username = data.get('username')
        email = data.get('email')
        WMusername = data.get('WMusername')

        if not all([username, email, WMusername]):
            return "Missing required fields", 400

        # Retrieve and process data
        olddf = retrieve_dataforfetchnew(username, email, WMusername)
        newdf = calculations(olddf)

        # Convert dataframe to JSON for response
        return jsonify(newdf.to_dict())  # Adjust based on how you want to return the data

    except Exception as e:
        print(f"Error: {e}")
        return str(e), 500

@app.route('/michlereportmakinggo', methods=['GET'])
def michlereportmakinggo():
    username = request.args.get('username')
    email = request.args.get('email')
    WMusername = request.args.get('WMusername')

    if not all([username, email, WMusername]):
        return "Missing required parameters", 400

    # Directly call the processing function
    olddf = retrieve_dataforfetchnew(username, email, WMusername)
    newdf1 = calculations(olddf)

    # Convert DataFrame to a list of dictionaries
    newdf = newdf1.to_dict(orient='records')

    # Render the HTML template to a string
    return render_template('michlereportmaking.html', newdf=newdf)

    


@app.route('/michlereportmakingdownload', methods=['GET'])
def michlereportmakingdownload():
    username = request.args.get('username')
    email = request.args.get('email')
    WMusername = request.args.get('WMusername')

    if not all([username, email, WMusername]):
        return "Missing required parameters", 400

    # Directly call the processing function
    olddf = retrieve_dataforfetchnew(username, email, WMusername)
    newdf1 = calculations(olddf)

    # Convert DataFrame to a list of dictionaries
    newdf = newdf1.to_dict(orient='records')

    # Render the HTML template to a string
    rendered_html = render_template('michlereportmaking.html', newdf=newdf)

    # Create a BytesIO object to hold the ZIP file content
    zip_buffer = io.BytesIO()

    # Create a ZIP file in memory
    with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
        # Add the HTML report to the ZIP file
        zip_file.writestr('michlereport.html', rendered_html)

        # Add other files if needed (for example, an additional text file)
        # zip_file.writestr('other_file.txt', 'Some content')

    # Seek to the beginning of the BytesIO object
    zip_buffer.seek(0)

    # Return the ZIP file as a response
    return send_file(
        zip_buffer,
        mimetype='application/zip',
        as_attachment=True,
        attachment_filename='files_archive.zip'
    )








#encription and decriptioni back end facing calles

@app.route('/encrypt', methods=['POST'])
def encrypt():
    data = request.json.get('data')
    encrypted_data = encrypt_data(data)
    return jsonify({"encrypted_data": encrypted_data})

@app.route('/decrypt', methods=['POST'])
def decrypt():
    encrypted_data = request.json.get('encrypted_data')
    decrypted_data = decrypt_data(encrypted_data)
    if decrypted_data:
        return jsonify({"decrypted_data": decrypted_data})
    else:
        return jsonify({"error": "Decryption failed"}), 400











from flask import Flask, send_file, jsonify, request
import os
import zipfile
import io
from google.cloud import storage
import logging
from encryption import decrypt_filezip
import tempfile

@app.route('/export-files', methods=['POST'])
def export_files():
    try:
        # Attempt to get JSON data from the request
        data = request.get_json()
        print("Data received:", data)

        if not data or 'WMusername' not in data:
            print("No data provided or data is invalid")
            logging.error("No data provided or data is invalid")
            return jsonify({'status': 'error', 'message': 'No data provided or data is invalid'}), 400

        WMusername = data['WMusername']
        print("WMusername extracted:", WMusername)

        if not WMusername:
            print("Username is required")
            logging.error("Username is required")
            return jsonify({'status': 'error', 'message': 'Username is required'}), 400

        bucket_name = "libertysolutionswiftwealth"
        blob_path = f"forWMconcole/pdfforreal/linkfilesforeachwm/{WMusername}/"

        print("Bucket name:", bucket_name)
        print("Blob path:", blob_path)

        # Initialize Google Cloud Storage client and get the bucket
        storage_client = storage.Client()
        bucket = storage_client.bucket(bucket_name)
        blobs = bucket.list_blobs(prefix=blob_path)

        print("Blobs listed")

        # Create a BytesIO buffer for the ZIP file
        zip_buffer = io.BytesIO()

        # Create a ZIP file
        with zipfile.ZipFile(zip_buffer, 'w', zipfile.ZIP_DEFLATED) as zip_file:
            for blob in blobs:
                # Extract the file name and extension from the blob path
                file_name_with_extension = blob.name.split('/')[-1]  # Get the last part after the last '/'
                print("File name with extension:", file_name_with_extension)

                if file_name_with_extension.endswith('.enc'):
                    # Extract the base file name without extension
                    base_file_name = file_name_with_extension.rsplit('.', 1)[0]
                    
                    # Create a temporary file path
                    with tempfile.NamedTemporaryFile(delete=False) as temp_file:
                        temp_file_path = temp_file.name
                        
                        # Download the file content and save to the temporary file
                        encrypted_data = blob.download_as_bytes()
                        with open(temp_file_path, 'wb') as temp_file_handle:
                            temp_file_handle.write(encrypted_data)
                        
                        # Decrypt the file content
                        decrypted_data = decrypt_filezip(temp_file_path)
                        
                        # Create a folder in the ZIP file named after the base file name
                        folder_name = base_file_name
                        
                        # Write the decrypted file content to the ZIP inside the folder
                        zip_file.writestr(f"{folder_name}/{file_name_with_extension.rstrip('.enc')}.csv", decrypted_data)
                        
                        # Remove the temporary file
                        os.remove(temp_file_path)

        zip_buffer.seek(0)

        # Return the ZIP file as an attachment
        return send_file(
            zip_buffer,
            download_name='files_archive.zip',
            as_attachment=True,
            mimetype='application/zip'
        )

    except Exception as e:
        print(f"Exception occurred: {str(e)}")
        logging.error(f"Exception occurred: {str(e)}")
        return jsonify({'status': 'error', 'message': str(e)}), 500


@app.route('/errorWithFinances.html')
def error_with_finances():
    return render_template('errorWithFinances.html')




if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
