import getpass, os
from imap_tools import MailBox, AND

imap_host_gmail = 'imap.gmail.com'  # Replace with the target email address
imap_host_outlook = 'outlook.office365.com'
                
def fetch_email_with_imap_tools_gmail():
    # print debug message
    print("Using gmail")

    # perform input username and password
    userVar, passwordVar = login_email()

    # save login result
    tempMailBox = MailBox(imap_host_gmail).login(userVar, passwordVar)
    # Print the login result
    if tempMailBox.login_result[0] != 'OK':
        # if login failed, print the error message
        print("Login failed: %s" % (tempMailBox.login_result[1]))
        exit(1)

    # If login is successful, print the success message
    print("Login successful!")
    wantedSubject = input("Subject (might be a keyword): ")
    print("fetching email pls wait...: " + wantedSubject)
    
    # making download attachment folder
    SAVE_DIR ="download_attachment"
    os.makedirs(SAVE_DIR, exist_ok=True)
    print(f"Attachments will be saved to: {os.path.abspath(SAVE_DIR)}")
    
    for selectedMail in tempMailBox.fetch(AND(subject=wantedSubject)):
        print(selectedMail.from_, selectedMail.date_str)
        # print(selectedMail.text)
        for selectedAttach in selectedMail.attachments:
            print(selectedAttach.filename)
            print(selectedAttach.content_type)
            file_path = os.path.join(SAVE_DIR, selectedAttach.filename)
            print(f"  Downloading: {selectedAttach.filename} to {file_path}")
            
            with open(file_path, 'wb') as f:
                f.write(selectedAttach.payload)
                print("    Downloaded successfully.")
                
def fetch_email_with_imap_tools_outlook():
    # print debug message
    print("Using outlook")
    
    # perform input username and password
    userVar, passwordVar = login_email()

    # save login result
    tempMailBox = MailBox(host=imap_host_outlook).login(userVar, passwordVar)
    # Print the login result
    if tempMailBox.login_result[0] != 'OK':
        # if login failed, print the error message
        print("Login failed: %s" % (tempMailBox.login_result[1]))
        exit(1)

    # If login is successful, print the success message
    print("Login successful!")
    wantedSubject = input("Subject (might be a keyword): ")
    print("fetching email pls wait...: " + wantedSubject)
    
    # making download attachment folder
    SAVE_DIR ="download_attachment"
    os.makedirs(SAVE_DIR, exist_ok=True)
    print(f"Attachments will be saved to: {os.path.abspath(SAVE_DIR)}")
    
    for selectedMail in tempMailBox.fetch(AND(subject=wantedSubject)):
        print(selectedMail.from_, selectedMail.date_str)
        # print(selectedMail.text)
        for selectedAttach in selectedMail.attachments:
            print(selectedAttach.filename)
            print(selectedAttach.content_type)
            file_path = os.path.join(SAVE_DIR, selectedAttach.filename)
            print(f"  Downloading: {selectedAttach.filename} to {file_path}")
            
            with open(file_path, 'wb') as f:
                f.write(selectedAttach.payload)
                print("    Downloaded successfully.")
    
    

def login_email():
    # getpass input for user
    userVar = input("Enter your email address: ")  

    # getpass input for password
    passwordVar = getpass.getpass()
    return userVar, passwordVar


