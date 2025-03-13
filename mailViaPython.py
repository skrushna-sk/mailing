import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_email(sender_email, sender_password, recipient_email, subject, message):
    try:
        # Setup the email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        # Connect to Gmail's SMTP server
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()  # Start TLS encryption
        server.login(sender_email, sender_password)  # Login to the email account
        server.send_message(msg)  # Send the email
        print("Email sent successfully!")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        server.quit()  # Close the connection

# Replace with your email credentials and details
sender_email = "skrushna.sk@gmail.com"
sender_password = ""  # Use your App Password here
recipient_email = "skrushna@live.com"
subject = "Test Email"
message = "This is a test email sent via Python."

send_email(sender_email, sender_password, recipient_email, subject, message)