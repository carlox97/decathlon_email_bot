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
    subject = 'Dischi Disponibili'
    body = 'https://www.decathlon.it/p/disco-ghisa-bodybuilding-28mm/_/R-p-7278?mc=1042303&c=NERO \n\n'

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

driver.get("https://www.decathlon.it/p/disco-ghisa-bodybuilding-28mm/_/R-p-7278?mc=1042303&c=NERO")
time.sleep(3)
driver.find_element(By.CSS_SELECTOR, ".didomi-continue-without-agreeing").click()   # rifiuta cookies

isp=0
cool_down = 1800  #sec

while True:

    # 5KG

    driver.find_element(By.CSS_SELECTOR, ".select:nth-child(4) .svg-icon").click()
    time.sleep(1)
    #driver.find_element(By.CSS_SELECTOR, "#option-product-size-selection-3 .stock").click()
    driver.find_element(By.ID, "option-product-size-selection-3").click()   # seleziona dimensione: 0 - 0.5KG; 1 - 1KG; 2 - 2KG; 3 - 5KG; 4 - 10KG; 5 - 20KG
    time.sleep(2)
    try:
        driver.find_element(By.XPATH,"//*[@id='app']/main/article/div[1]/div[6]/section/article/div/button").is_displayed()
        #driver.find_element(By.CSS_SELECTOR, ".cta--block").is_displayed()
    except:
        time.sleep(120)
    else:
        send_mail()
        isp=1

    # 10KG

    driver.find_element(By.CSS_SELECTOR, ".select:nth-child(4) .svg-icon").click()
    time.sleep(1)
    #driver.find_element(By.CSS_SELECTOR, "#option-product-size-selection-3 .stock").click()
    driver.find_element(By.ID, "option-product-size-selection-4").click()   # seleziona dimensione: 0 - 0.5KG; 1 - 1KG; 2 - 2KG; 3 - 5KG; 4 - 10KG; 5 - 20KG
    time.sleep(2)
    try:
        driver.find_element(By.XPATH,"//*[@id='app']/main/article/div[1]/div[6]/section/article/div/button").is_displayed()
        #driver.find_element(By.CSS_SELECTOR, ".cta--block").is_displayed()
    except:
        time.sleep(120)
    else:
        send_mail()
        isp=1

    if isp:
        time.sleep(cool_down)
        isp=0

    driver.refresh()
    time.sleep(2)
