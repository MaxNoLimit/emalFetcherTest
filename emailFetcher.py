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

def fetch_email_with_imap_tools_specific_subject():
    # perform input username and password
    userVar, passwordVar = login_email()

    # save login result
    tempMailBox = MailBox(imap_host).login(userVar, passwordVar)
    # Print the login result
    if tempMailBox.login_result[0] != 'OK':
        # if login failed, print the error message
        print("Login failed: %s" % (tempMailBox.login_result[1]))
        exit(1)

    # If login is successful, print the success message
    print("Login successful!")
    print("fetching email pls wait...")
    
    # start looping to search a certain email
    nCount = 0
    for msg in tempMailBox.fetch():
        nCount += 1
        print(nCount)
        if msg.subject == 'Lamaran Posisi Data Scientist – William Deli':
            print(msg.from_, msg.date_str)
            print(msg.text)
            for atth in msg.attachments:
                print(atth.filename)
                print(atth.content_type)
                
def fetch_email_with_imap_tools():
    # perform input username and password
    userVar, passwordVar = login_email()
    wantedSubject = input("Subject (might be a keyword): ")

    # save login result
    tempMailBox = MailBox(imap_host).login(userVar, passwordVar)
    # Print the login result
    if tempMailBox.login_result[0] != 'OK':
        # if login failed, print the error message
        print("Login failed: %s" % (tempMailBox.login_result[1]))
        exit(1)

    # If login is successful, print the success message
    print("Login successful!")
    print("fetching email pls wait...: " + wantedSubject)
    
    # new method
    # selectedMail = tempMailBox.fetch(AND(subject='Lamaran Posisi Data Scientist'))
    for selectedMail in tempMailBox.fetch(AND(subject=wantedSubject)):
    # for selectedMail in tempMailBox.fetch(AND(subject='Lamaran Posisi')):
        print(selectedMail.from_, selectedMail.date_str)
        print(selectedMail.text)
        for selectedAttach in selectedMail.attachments:
            print(selectedAttach.filename)
            print(selectedAttach.content_type)

def login_email():
    # getpass input for user
    userVar = input("Enter your email address: ")  

    # getpass input for password
    passwordVar = getpass.getpass()
    return userVar, passwordVar


