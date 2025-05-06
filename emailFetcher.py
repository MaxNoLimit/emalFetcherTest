# from imaplib import IMAP4_SSL
import getpass, imaplib

imap_host = 'imap.gmail.com'  # Replace with the target email address

if __name__ == "__main__":
    # Connect to the email server
    emailHandler = imaplib.IMAP4_SSL(imap_host)

    # getpass input for user
    userVar = input("Enter your email address: ")  # Prompt for the email address

    # getpass input for password
    passwordVar = getpass.getpass()  # Prompt for the password

    # Login to the email account
    print("Logging in with %s and %s" % (userVar, passwordVar))
    emailHandler.login(userVar, passwordVar)


    emailHandler.select('Inbox')
    typ, data = emailHandler.search(None, 'ALL')
    for num in data[0].split():
        typ, data = emailHandler.fetch(num, '(RFC822)')
        print('Message %s\n%s\n' %(num, data[0][1]))
    emailHandler.close()
    emailHandler.logout()
