import smtplib

my_email = "lockwood.ethan@yahoo.com"
password = "fdniltzrohburhxk"
smtp_host = "smtp.mail.yahoo.com"

connection = smtplib.SMTP_SSL(smtp_host, 465, timeout=10)
connection.login(user=my_email, password=password)
connection.sendmail(from_addr=my_email, to_addrs="maddiejee@gmail.com", msg="hello")
connection.close()