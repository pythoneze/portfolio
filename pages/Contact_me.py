import streamlit as st
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()

# Function to send email
def send_email(user_email, message):
    try:
        # Gmail SMTP server configuration
        smtp_server = 'smtp.gmail.com'
        smtp_port = 587
        sender_email = os.getenv('GMAIL_USER')
        sender_password = os.getenv('GMAIL_PASSWORD')

        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = sender_email
        msg['Subject'] = 'Contact Form Submission'

        body = f'From: {user_email}\nMessage:\n{message}'
        msg.attach(MIMEText(body, 'plain'))

        # Connect to the SMTP server
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
            server.login(sender_email, sender_password)
            server.send_message(msg)
            st.success('Message sent successfully!')
    except Exception as e:
        st.error(f'Failed to send message. Error: {e}')

st.header("Contact Me")

with st.form(key="email_form"):
    user_email = st.text_input("Your email address")
    message = st.text_area("Your message")
    submit_button = st.form_submit_button("Submit")

    if submit_button:
        send_email(user_email, message)
