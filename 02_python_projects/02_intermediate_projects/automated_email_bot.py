## Automated Email Bot
## This script prepares and sends an email message using SMTP when credentials are available.
## Without credentials, it runs in dry-run mode and prints the message instead.

import os
import smtplib
from email.message import EmailMessage


def send_email(recipient: str, subject: str, body: str) -> str:
    sender = os.getenv("EMAIL_USERNAME")
    password = os.getenv("EMAIL_PASSWORD")
    smtp_server = os.getenv("EMAIL_SMTP_SERVER", "smtp.gmail.com")
    smtp_port = int(os.getenv("EMAIL_SMTP_PORT", "587"))

    if not sender or not password:
        print("Email credentials were not found. Running in dry-run mode.")
        print("To:", recipient)
        print("Subject:", subject)
        print("Body:", body)
        return "dry-run"

    message = EmailMessage()
    message["Subject"] = subject
    message["From"] = sender
    message["To"] = recipient
    message.set_content(body)

    try:
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender, password)
            server.send_message(message)
        print("Email sent successfully.")
        return "sent"
    except Exception as exc:
        print(f"Email sending failed: {exc}")
        return "failed"


if __name__ == "__main__":
    recipient = input("Enter recipient email: ").strip() or "example@email.com"
    subject = "Python Automation Reminder"
    body = "This is a test message from the automated email bot."

    send_email(recipient, subject, body)
