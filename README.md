# Birthday Email Sender
A simple Python application designed to send automated birthday wishes via email. Utilizing smtplib, pandas, and datetime, it checks a CSV file for birthdays that match the current date and sends a personalized email using one of several customizable templates.

## Features
- Automated Email Sending: Sends out birthday wishes without manual intervention.
- Customizable Letter Templates: Personalize birthday messages using template files.
- CSV Integration: Manages birthdays and email addresses using a CSV file.

## Dependencies
- Pandas: For reading and processing the CSV file.
- Datetime: For handling dates.
- smtplib: For sending emails through an SMTP server.

## Setup
1. Ensure Python 3.x is installed on your system.

2. Install the required libraries with pip:

```sh
pip install pandas

```

3. Modify MY_EMAIL and MY_PASSWORD in the main.py script to match your email credentials.

4. Add the birthday data to a birthdays.csv file in the project directory.

5. Place your email templates in the letter_templates directory and ensure they are named in the format letter_1.txt, letter_2.txt, etc.

## Usage
- Run main.py to start the email sender. It will check the current date against the birthdays listed in birthdays.csv.
- f there's a match, it will send a customized email to the birthday person using a random template from the letter_templates directory.


## Note
Ensure that you have allowed less secure apps to access your email if you are using Gmail. This can be configured in your Gmail account settings. It's recommended to use app-specific passwords for added security.
