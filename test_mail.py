import smtplib,ssl

from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.header import Header

#郵件主旨
sender ="f59xomk7@gmail.com"
receiver = ["wind8087@gmail.com","fwind8087@yahoo.com"]
password = "wsvm phrq hvhg fvav"

for r in receiver:
    msg = MIMEMultipart()
    msg["From"] = sender
    msg["To"] = r
    msg["Subject"] = Header("Test send email","utf-8").encode()

    body = "This is send by python"

    msg_text = MIMEText(body)
    msg.attach(msg_text)

    #伺服器設定


    with smtplib.SMTP("smtp.gmail.com",587) as s:
        s.starttls()
        s.login(msg["From"],password)
        s.sendmail(msg["From"],msg["To"],msg.as_string())
    print("success send mail!")