import smtplib
import ssl
import json

host = 'smtp.gmail.com'
port = 465

with open('data/creds.json', 'r') as file:
    creds = json.loads(file.read())
    username = creds['username']
    password = creds['password']

receiver = 'robert.lagrasse@gmail.com'
context = ssl.create_default_context()

message = '''
This is a test
Don't be alarmed.
This is only a test.
'''

with smtplib.SMTP_SSL(host, port, context=context) as server:
    server.login(username, password)
    server.sendmail(username, receiver, message)