import smtplib          # Simple Mail Transfer Protocol for emails
import os               # For file path and file existence checks
import csv              # To read email addresses from csv file
from email.mime.multipart import MIMEMultipart
# for Creating multipart email messages
from email.mime.text import MIMEText
# for adding plain text to eamil Body


SMTP_SERVER = 'smtp.gmail.com'
SMTP_PORT = 587
SENDER_EMAIL = 'asschandrakiran@gmail.com'
SENDER_PASSWORD = 'fmvw lipd dkno bfew'

def send_email(to_email,subject,body):
    try:                            # try used because any network issue or someother issues may occure
        msg = MIMEMultipart()
        msg['From'] = SENDER_EMAIL
        msg['To'] = to_email
        msg['Subject'] = subject
        msg.attach(MIMEText(body,'Plain'))

        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(SENDER_EMAIL, SENDER_PASSWORD)
        server.sendmail(SENDER_EMAIL, to_email, msg.as_string())
        server.quit()
        print(f"Email Sent to {to_email}")

    except Exception as e:  
        print(f"Error Sending Email to {to_email}: {e}")

def send_bulk_emails(csv_file, subject, body):
    try:
        csv_path = os.path.abspath(csv_file)
        if not os.path.exists(csv_path):
            print(f'Error: CSV File {csv_file} not found')
            return
        
        with open(csv_path, newline = "", encoding = "utf-8") as file:
            reader = csv.reader(file)
            # next(reader,None) used to skip first line
            for row in reader:
                if row:
                    email = row[0]
                    send_email