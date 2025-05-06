# from imaplib import IMAP4_SSL
import getpass, imaplib



if __name__ == "__main__":
    emailHandler = imaplib.IMAP4_SSL('imap.gmail.com')
    emailHandler.login(getpass.getuser(), getpass.getpass())
    emailHandler.select('inbox')
    typ, data = emailHandler.search(None, 'ALL')
    for num in data[0].split():
        typ, data = emailHandler.fetch(num, '(RFC822)')
        print('Message %s\n%s\n' %(num, data[0][1]))
    emailHandler.close()
    emailHandler.logout()
