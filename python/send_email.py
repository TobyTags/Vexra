from email.mime.base import MIMEBase
from email import encoders
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

def email():
    def send_email_with_attachment(filepath):
        # Email details
        sender_email = 'info.vexra@gmail.com'  # Replace with your email
        password = 'djhb kpez pwtq zbbf'  # Replace with your email account password

        # List of recipient email addresses
        receiver_emails = ['tobytangney@gmail.com']  # Add more emails as needed

        # michaeljscahill@gmail.com, arthur.elveden@student.manchester.ac.uk

        # Email subject and body
        subject = 'TTTTT'
        body = 'This is end full automated extraction output \n attached is a pdf document generated from extracted data from the questionnaire \n\n this is a bot submission'

        # Create the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = ', '.join(receiver_emails)
        msg['Subject'] = subject

        # Attach the email body
        msg.attach(MIMEText(body, 'plain'))

        # Attach the file
        try:
            with open(filepath, 'rb') as file:
                part = MIMEBase('application', 'octet-stream')
                part.set_payload(file.read())
                encoders.encode_base64(part)
                part.add_header(
                    'Content-Disposition',
                    f'attachment; filename={"Client_Report.pdf"}',  # Ensure the file has a proper extension
                )
                msg.attach(part)
        except Exception as e:
            print(f'Error reading attachment file: {e}')
            return

        # Send the email
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)  # For Gmail
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_emails, msg.as_string())
            print('Email sent successfully!')
        except Exception as e:
            print(f'Error sending email: {e}')
        finally:
            server.quit()

    # Path to the PDF file
    filepath = "/Users/Toby/Desktop/Patch/OUTPUT5.pdf"
    send_email_with_attachment(filepath)



# # imports for email seending (automated)
# import smtplib
# from email.mime.multipart import MIMEMultipart
# from email.mime.text import MIMEText
# from email.mime.base import MIMEBase
# from email import encoders








