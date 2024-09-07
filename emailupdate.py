import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

spoken_text = "pheonix can you please email Owen hey whats up is this working"

contactsPeople = ["Owen","Ozone"]
contactsNumbers = ["1234","4321"]
contactsEmails = ["markoffowen9@gmail.com","OzoneGamez3@gmail.com"]
sender_email = "markoffowen9@gmail.com"
sender_password = "gush ygqa npag naxx"
subject = " "


if "pheonix can you please email" in spoken_text:
    question = spoken_text.split("pheonix can you please email", 1)[1].strip()
    question = question.split(" ")
    receiver_email = contactsEmails[contactsPeople.index(question[0])]
    question.pop(0)
    body = ' '.join(question)

    # Create a multipart message
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject

    # Attach the body with the msg instance
    msg.attach(MIMEText(body, 'plain'))


    # Connect to the server and send the email
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, sender_password)
    server.sendmail(sender_email, receiver_email, msg.as_string())
    print("Email sent successfully!")