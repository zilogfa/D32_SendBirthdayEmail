# D32: Sending Birthday Email - Dev: Ali Jafarbeglou 2022
"""
Birthday Email Sender
Automated Birthday Emails with Customizable Templates
This console app is written in Python and uses SMTPLIB, Pandas and DateTime to generate and send automated birthday emails with letter templates. You can provide people’s information as a CSV file to automate sending birthday emails on their birthday. The CSV file should include the name, birthday month, date and year, and their email.
• Automated email sending on people’s birthdays
• Customizable letter templates
• Easy to use CSV file format for people’s information
"""

import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = "zilogfa@gmail.com"
MY_PASSWORD = "sakseyklbmhbczcl"

today = dt.datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"letter_templates/letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subjects: Happy Birthday\n\n{contents}"
        )


