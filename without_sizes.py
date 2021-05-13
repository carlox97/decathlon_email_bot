from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def send_mail():
    import smtplib
    from datetime import datetime

    gmail_user = 'YOUR_GMAIL'
    gmail_password = 'YOUR_GENERATED_PASSWORD'

    sent_from = gmail_user
    to = ['MAIL_BEING_NOTIFIED']
    subject = 'Billy da 2m disponibile'
    body = 'https://www.decathlon.it/p/bilanciere-bodybuilding-2m-28mm/_/R-p-9291?mc=8289900 \n\n'

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

cool_down = 1800  #sec, ovvero mezzora di pausa dopo una mail
cadenza = 120 #sec, ovvero ogni quanto controllo se ci sono i dischi

chrome_options = Options()
chrome_options.add_argument("--headless")
driver = webdriver.Chrome("C:\web\chromedriver.exe",options=chrome_options)

driver.get("https://www.decathlon.it/p/bilanciere-bodybuilding-2m-28mm/_/R-p-9291?mc=8289900")    #decathlon link
driver.set_window_size(1296, 1400)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#didomi-notice-agree-button > span")))
driver.find_element(By.CSS_SELECTOR, "#didomi-notice-agree-button > span").click()

while True:

    time.sleep(1)

    if driver.find_element(By.ID, "ctaButton").is_displayed():
        send_mail()
        time.sleep(cool_down-cadenza)

    time.sleep(cadenza)
    driver.refresh()
