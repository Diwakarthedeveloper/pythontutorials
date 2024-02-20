from tkinter.messagebox import YES
import requests #http requests

from bs4 import BeautifulSoup #web scrapping

#send the email
import smtplib email, getpass, imaplib, os

#email body
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

#system date and time manipulation
import datetime
now= datetime.datetime.now()

#emaill cotent body

content = '' # global object
#extracting Hacker news Stories
def extract_news(url):
    print('Extracting Hacker news Stories')
    cnt = ''
    cnt+= ('<b> HN top news: </b> \n '+'<br>'+'-'*50+'<br>')
    response = requests.get(url)
    content = response.content  # this content is a local content and diffrent from the above global one
    soup = BeautifulSoup(content, 'html.parser')
    for i, tag in enumerate(soup.find_all('td',attrs={'class': 'title', 'valign': ''})):
        cnt += ((str(i+1)+' :: '+tag.text+"\n" + '<br>') if tag.text!='More' else '')

#print(tag,prettify) #find all('span', attrs={'class': 'sitestr'}))
    return(cnt)

cnt = extract_news('https://news.ycombinator.com/')
content += cnt
content += ('<br>------<br>')
content +=('<br><br>ENd of Message')

#lets send a email
print('composing email ')

#update your email details

SERVER = 'smtp.gmail.com' #my smtp server
SSL = YES
PORT = 587 #my port number
From = 'djha4635@gmail.com' # my email id
TO = 'djha4635@gmail.com' #receipient email id
PASS = 'password@123' # email password

# fp = open(file_name, 'rb')
# Create a text/plain message
# msg = MINEText('')
msg = MIMEMultipart()

#msg.add_header('Content-Disposition','attachemnet', filename='empty.txt')
msg['Subject'] = 'Top News Storoes HN [Automated Email]' + ' '+ str(now.day) + '-' + str(now.month) + '-' + str(now.year)
msg['From'] = From
msg['To'] = TO
msg.attach(MIMEText(content, 'html'))
#fp.close
print('Initiating Server')
server = smtplib.SMTP(SERVER, PORT)

#server = smtplib.SMTP SSL('smtp.gmail.com', 465)
server.set_debuglevel(1)
server.ehol()
server.starttls(1)
server.login(FROM, PASS)
server.sendmail(FROM, TO, msg.as_string())

print('Email Sent')

server.quit()