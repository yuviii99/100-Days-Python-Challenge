import pandas
import smtplib
import datetime
import random

MY_USERNAME = "Enter yor email address"
PASSWORD = "Enter your password"
RECEIVER_EMAIL = "To whom you want to send email"

birthday_dict = pandas.read_csv("birthdays.csv").to_dict(orient="records")

current_month = datetime.datetime.now().month
current_day = datetime.datetime.now().day

for dates in birthday_dict:
    if dates['month'] == current_month and dates['day'] == current_day:
        email_id = dates['email']
        name = dates['name']
        letter_choice = random.randint(1, 3)
        with open(f"letter_templates/letter_{letter_choice}.txt", "r") as letter_file:
            letter_contents = letter_file.read()
        new_letter_contents = letter_contents.replace("[NAME]", name)

        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=MY_USERNAME, password=PASSWORD)
            connection.sendmail(from_addr=MY_USERNAME, to_addrs=RECEIVER_EMAIL, msg=f"Subject:HAPPY BIRTHDAY\n\n{new_letter_contents}")
