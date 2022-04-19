import smtplib
import random
import datetime

MY_USERNAME = "Enter yor email address"
PASSWORD = "Enter your password"
RECEIVER_EMAIL = "To whom you want to send email"

# <------------------------------ Get current day of the week ------------------------------>
current_day = datetime.datetime.now().weekday()
if current_day == 1:
    # <------------------------------ Get quotes from file ------------------------------>
    with open("quotes.txt", "r") as quotes_file:
        quotes_list = quotes_file.readlines()
        quote = random.choice(quotes_list)

    # <------------------------------ Send an email to myself ------------------------------>
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_USERNAME, password=PASSWORD)
        connection.sendmail(from_addr=MY_USERNAME, to_addrs=RECEIVER_EMAIL,
                            msg=f"Subject:Monday Motivation\n\n{quote}")
