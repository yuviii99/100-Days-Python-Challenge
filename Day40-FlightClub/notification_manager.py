from twilio.rest import Client
import smtplib

TWILIO_SID = "YOUR TWILIO SID"
TWILIO_AUTH_TOKEN = "TWILIO_AUTH_TOKEN"
TWILIO_NUMBER = "TWILIO_NUMBER"
TWILIO_VERIFIED_NUMBER = "YOUR_NUMBER"
MY_USERNAME = "YOUR_EMAIL"
MY_PASSWORD = "YOUR_PASSWORD"


class NotificationManager:
    def __init__(self):
        self.client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

    def send_sms(self, message):
        message = self.client.messages.create(
            body=message,
            from_=TWILIO_NUMBER,
            to=TWILIO_VERIFIED_NUMBER
        )
        print(message.sid)

    def send_emails(self, message, to_emails, google_flight_link):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_USERNAME, password=MY_PASSWORD)
            for email in to_emails:
                connection.sendmail(
                    from_addr=MY_USERNAME,
                    to_addrs=email,
                    msg=f"Subject: New Low Price Flight!\n\n{message}\n{google_flight_link}".encode('utf-8')
                )
