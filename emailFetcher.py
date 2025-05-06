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
    print("Logging in into %s" % (userVar))
    loginResult = emailHandler.login(userVar, passwordVar)

    # Print the login result
    if loginResult[0] != 'OK':
        # if login failed, print the error message
        print("Login failed: %s" % (loginResult[1]))
        exit(1)

    # If login is successful, print the success message
    print("Login successful!")

    emailHandler.select('Inbox')

    tmp, data = emailHandler.search(None, 'ALL')
    # tmp, data = emailHandler.fetch(data[0].split()[0], '(RFC822)')
    # print("data: %s" % (data))

    tmp, data = emailHandler.fetch(data[0].split()[0], '(RFC822)')
    # Print the email data
    print("data: \n%s" % (data[0][1]))

    emailHandler.close()
    emailHandler.logout()
