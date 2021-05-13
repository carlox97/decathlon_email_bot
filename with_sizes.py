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
    subject = 'Dischi 5KG Disponibili'
    body = 'https://www.decathlon.it/p/disco-ghisa-bodybuilding-28mm/_/R-p-7278?currentPage=1&filter=all&mc=1042303&c=NERO&orderId=it622328573 \n\n'

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
driver = webdriver.Chrome("C:\web\chromedriver.exe")

driver.get("https://www.decathlon.it/p/disco-ghisa-bodybuilding-28mm/_/R-p-7278?currentPage=1&filter=all&mc=1042303&c=NERO&orderId=it622328573")
driver.set_window_size(1296, 1400)
element = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, "#didomi-notice-agree-button > span")))
driver.find_element(By.CSS_SELECTOR, "#didomi-notice-agree-button > span").click()

cool_down = 1800  #sec

while True:

    time.sleep(1)

    # 5KG

    driver.find_element(By.CSS_SELECTOR, ".sizes__button").click()
    driver.find_element(By.CSS_SELECTOR, ".sizes__size:nth-child(4) > .sizes__info").click()
    if driver.find_element(By.ID, "ctaButton").is_displayed():
        send_mail()
        time.sleep(cool_down)
        driver.refresh()
        time.sleep(1)

   # 20KG

    driver.find_element(By.CSS_SELECTOR, ".sizes__button").click()
    driver.find_element(By.CSS_SELECTOR, ".sizes__size:nth-child(6) > .sizes__info").click()
    if driver.find_element(By.ID, "ctaButton").is_displayed():
        send_mail()
        time.sleep(cool_down)
        driver.refresh()
        time.sleep(1)

    time.sleep(120)
    driver.refresh()
