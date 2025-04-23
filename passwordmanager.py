import smtplib
from email.utils import make_msgid
import mimetypes
from email.message import EmailMessage
import random
import string

def inputChoice():
    choice = int(input('chose your options: 1, login  or 2, sign up'))
    print(choice)
    while choice != 1 or choice !=2:
        choice = input('invalid choice try again')
    
    return choice


def newAccount():

    email = input("what is your email")
    def sendVerification(email):
        length = 5
        characters = string.ascii_letters + string.digits
        code = ''.join(random.choice(characters) for i in range(length))
        code = EmailMessage()
        code['Subject'] = 'Verification code'
        code['From'] = "Password Manager"
        code['To'] = email
        code.set_content(body)
        with smtplib.SMTP_SSL('smtp.gmail.com',465) as server:
            server.login('Passoword Manager', 'Lgv')
            server.send_message(code)
    
    sendVerification()  

    
    return email
    
    
def login():
    
    user = input("what is your username")
    password = input("what is your password")
    accountName = input("what is your accountName")
    
    return user, password, accountName

choice = inputChoice()
