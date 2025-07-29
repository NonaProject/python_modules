# Nona Project - Python web toolbox

# Basic File Utils

def create_file(filename): # Creates An empty file at dir
    try:
        with open(filename, 'w') as f:
            f.write('')
    except Exception as e:
        print(f'Error Raised {e}')

def overwrite_file_content(filename, content): # Over-Writes the content of a given file
    try:
        with open(filename, 'w') as f:
            f.write(content)
    except Exception as e:
        print(f'Error Raised {e}')

def get_file_content(filename): # Returns the content of the file
    try: 
        with open(filename, 'r') as f:
            return f.read()
    except Exception as e:
        print(f'Error raised {e}')

# Email Handling

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


# Returns a dictionary that contains sender/receiver credentials
def configure_email(sender: str, receiver: str, password: str) -> dict:
    return {"sender": sender, "receiver": receiver, "password": password}

# Sends Email message 
def send_message(credentials: dict, subject: str, content: str) -> str:
    
    # Configures email message
    message = MIMEMultipart()
    message["From"] = credentials['sender']
    message["To"] = credentials['receiver']
    message["Subject"] = subject
    body = content
    message.attach(MIMEText(body, "plain"))

    # Attempts to connect to server and send message

    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(credentials['sender'], credentials['password'])
            server.sendmail(credentials['sender'], credentials['receiver'], message.as_string())
            return 'Successful Send!'
    except Exception as e:
        return f"Didn't send, error {e}"

