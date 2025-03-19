import smtplib, random
from datetime import datetime

my_email = "email"
password = "password"

now = datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("~/MondayMorningMotivation/quotes.txt", "r") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
        
        with smtplib.SMTP("smtp.mail.yahoo.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="other_email@gmail.com",
                msg=f"Subject:Monday Morning Motivational Quote\n\n{quote}"
            )