# from imaplib import IMAP4_SSL
import getpass, imaplib
from imap_tools import MailBox, AND



imap_host = 'imap.gmail.com'  # Replace with the target email address

def fetch_email_with_imaplib():
    # Connect to the email server
    emailHandler = imaplib.IMAP4_SSL(imap_host)

    # perform input username and password
    userVar, passwordVar = login_email()

    # Login to the email account
    print("Logging in into %s" % (userVar))
    loginResult = emailHandler.login(userVar, passwordVar)

    # Print the login result
    if loginResult[0] != 'OK':
        # if login failed, print the error message
        print("Login failed: %s" % (loginResult[1]))
        exit(1)

    # If login is successful, print the success message
    print("Login successful!")

    # Select Inbox
    emailHandler.select('Inbox')

    tempFetchedMsg = emailHandler.fetch()
    

    emailHandler.close()
    emailHandler.logout()

def fetch_email_with_imap_tools():
    # perform input username and password
    userVar, passwordVar = login_email()

    # save login result
    tempMailBox = MailBox(imap_host).login(userVar, passwordVar)

    for msg in tempMailBox.fetch(limit=5):
        print(msg.date, msg.subject)

def login_email():
    # getpass input for user
    userVar = input("Enter your email address: ")  

    # getpass input for password
    passwordVar = getpass.getpass()
    return userVar, passwordVar


