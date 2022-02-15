import smtplib
import time
from bs4 import BeautifulSoup
import requests

url = "https://dia2.units.it/didattica/orario/ingegneria/" #the url that you need to check
dish = "[<h2>ORARIO DI PROSSIMA PUBBLICAZIONE</h2>]"  #a HTML line that will change

#the next 2 lines convert dish to a bs4 element resultSet object
dish = BeautifulSoup(dish, 'html.parser')
dish = dish.find_all('h2') #tutto sto casino per avere oggetti dello stesso tipo


#get the HTML of the page, look for the line saved in the dish variable and return true if found
def checkSite():
    r = requests.get(url)
    html = BeautifulSoup(r.text, 'html.parser')
    soup = html.find_all('h2')
    return soup == dish

def sendMail():
    sender = smtplib.SMTP('smtp.gmail.com', 587) #i used gmail but you can use any mail, look at the smtplib documentation
    sender.ehlo()
    sender.starttls()
    sender.login('SENDER_MAIL', 'MAIL_PASSWORD') #for google you have to create a password for the app
    x = sender.sendmail('SENDER_MAIL', 'RECIEVER_MAIL', 'Subject: SUBJECT\n\nMAIL_TEXT')
    print(x) #if it print something that is not {} then the mail wasn't send
    sender.quit()

#check every 10 minutes if there are changes, 
while(checkSite):
    time.sleep(600)
sendMail()
