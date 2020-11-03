import smtplib
import imaplib
import mailbox
import base64
import email
import re
from email.message import EmailMessage
from email.headerregistry import Address


def send_email(message):
    #content = 'Robot has finished cleaning ' + str(count)
    #content += ' Ranarr Weeds, netting ' + str((count * potion_price) - (count * ranarr_price)) + 'GP profit'

    mail = smtplib.SMTP('smtp.gmail.com', 587)

    mail.ehlo()

    mail.starttls()

    #Login
    mail.login('taubinrunescape@gmail.com', 'NeverEatSoggyWaffles')
    mail.sendmail('taubinrunescape@gmail.com', '6035082773@vtext.com', message)
    mail.close()
    print('Email sent!')
    return True


def read_emails():
    global current_email

    fdin = open('last_email.txt', 'r')
    prev_com = fdin.read()
    fdin.close()
    fdout = open('last_email.txt', 'w')
    #print(fdin.read())
    #exit()

    username = 'taubinrunescape@gmail.com'
    password = 'NeverEatSoggyWaffles'

    imap = imaplib.IMAP4_SSL('imap.gmail.com')
    imap.login(username, password)

    imap.select('Inbox')

    typ, data = imap.uid('search', None, 'ALL')

    inbox_item_list = data[0].split()

    most_recent = inbox_item_list[-1]

    result, email_data = imap.uid('fetch', most_recent, '(RFC822)')

    raw_email = email_data[0][1].decode('utf-8')

    email_message = email.message_from_string(raw_email)

    latest_email = email_message.get_payload()
    latest_email = re.sub(r"[\n\t\s]*", "", latest_email)
    #print(latest_email, prev_com)
    #exit()

    if latest_email != prev_com:
        send_email(('Mode set to ' + latest_email))

    if latest_email == 'Logout':
        fdout.write(latest_email)
        fdout.close()
        #print('Not the same')
        #click(2543, 14, left)
        #sleep(0.2)
        #click(1226, 729, left)
        #sleep(0.1)
        send_email('Successfully Logged Out')
        imap.close()
        imap.logout()
        return True
    if latest_email == 'Create':
        fdout.write(latest_email)
        fdout.close()
        print('Back to grinding')
        imap.close()
        imap.logout()
        return False
    imap.close()
    imap.logout()
    #print()


if __name__ == '__main__':
    done = False
    while not done:
        done = read_emails()
    exit()