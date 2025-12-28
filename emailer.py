import smtplib
from email.mime.text import MIMEText
from datetime import datetime

EMAIL_FROM = os.getenv("EMAIL_FROM")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
EMAIL_TO = EMAIL_FROM

def send_email(jobs):
    body = ""
    for job in jobs:
        body += (
            f"{job['title']}\n"
            f"{job['company']}\n"
            f"{job['location']}\n"
            f"{job['link']}\n\n"
        )

    msg = MIMEText(body)
    msg["Subject"] = f"🇺🇸 Verified QA Jobs – {datetime.now().strftime('%Y-%m-%d')}"
    msg["From"] = EMAIL_FROM
    msg["To"] = EMAIL_TO

    with smtplib.SMTP("smtp.gmail.com", 587) as server:
        server.starttls()
        server.login(EMAIL_FROM, EMAIL_PASSWORD)
        server.send_message(msg)

