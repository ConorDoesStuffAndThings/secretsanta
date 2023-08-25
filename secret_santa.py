import random
import smtplib
from email.mime.text import MIMEText

EMAIL_HOST = 'host'
EMAIL_PORT = 587
EMAIL_USER = 'email@email.com'
EMAIL_PASSWORD = 'password'

participants = [
    {'name': 'Jason', 'email': 'jason.p.p.hanafin@gmail.com'},
    {'name': 'Paddy', 'email': 'hayespaddy96@gmail.com'},
    {'name': 'Conor', 'email': 'conorhartigan13@gmail.com'},
    {'name': 'Ryan', 'email': 'ryan@email.com'},
    {'name': 'Pepi', 'email': 'elenahorgan2@gmail.com'},
    {'name': 'Luna', 'email': 'uselesslana@gmail.com'},
    {'name': 'Ben', 'email': 'benlenihan99@gmail.com'},
]

random.shuffle(participants)

assignments = {}
for i in range(len(participants)):
    giver = participants[i]
    receiver = participants[(i + 1) % len(participants)]
    assignments[giver['name']] = receiver['name']

for giver, receiver in assignments.items():
    message = f"Hello {giver}!\n\nYou are the Secret Santa for {receiver}.\nPlease buy a thoughtful gift for them!\n\nBest regards,\nSecret Santa Organizer"

    msg = MIMEText(message)
    msg['Subject'] = 'Secret Santa Assignment'
    msg['From'] = EMAIL_USER
    msg['To'] = giver

    try:
        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_USER, EMAIL_PASSWORD)
        server.sendmail(EMAIL_USER, [giver], msg.as_string())
        server.quit()
        print(f"Email sent to {giver}")
    except Exception as e:
        print(f"Error sending email to {giver}: {e}")
