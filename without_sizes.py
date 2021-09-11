from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

def send_mail():
    import smtplib
    from datetime import datetime

    gmail_user = 'YOUR_GMAIL'
    gmail_password = 'YOUR_GENERATED_PASSWORD'

    sent_from = gmail_user
    to = ['MAIL_BEING_NOTIFIED']
    subject = 'Articolo Disponibile'
    body = 'https://www.decathlon.it/p/manubrio-bodybuilding-35cm-28mm/_/R-p-7260?mc=1041986 \n\n'

    email_text = """From: %s
To: %s
Subject: %s

%s
""" % (sent_from, ", ".join(to), subject, body)
    try:
        server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, email_text)
        server.close()


        now = datetime.now()
        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
        print ('Email sent!', dt_string)
    except:
        print ('Something went wrong...')
        
print('running...')

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("C:\web\chromedriver.exe",options=chrome_options)

driver.get("https://www.decathlon.it/p/manubrio-bodybuilding-35cm-28mm/_/R-p-7260?mc=1041986")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".didomi-continue-without-agreeing").click()   # rifiuta cookies

cool_down = 1800  # sec

while True:

    try:
        #driver.find_element(By.CSS_SELECTOR, ".cta--block").is_displayed()
        driver.find_element(By.XPATH,"//*[@id='app']/main/article/div[1]/div[5]/section/article/div/button").is_displayed() # div[1]/div[X]: X può variare per diversi articoli. Se non si è sicuri togliere il commento alla riga sopra e commentare questa.
    except:
        time.sleep(120)
    else:
        send_mail()
        time.sleep(cool_down)

    driver.refresh()
    time.sleep(4)

