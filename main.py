from selenium import webdriver
from selenium.webdriver.common.by import By
import time
from internet import intern

test = intern()

Username = input("What is your twitter username or email? ")
Password = input("What is your twitter password? ")


options = webdriver.ChromeOptions()
options.add_experimental_option('detach', True)


driver = webdriver.Chrome(options=options)

driver.get("https://twitter.com/i/flow/login?redirect_after_login=%2F")

time.sleep(4)
username = driver.find_element(
    By.CLASS_NAME,
    'r-30o5oe'
    )

next = driver.find_element(
    By.CSS_SELECTOR,
    '#layers > div > div > div > div > div > div > div.css-1dbjc4n.r-1awozwy.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv > div.css-1dbjc4n.r-1867qdf.r-1wbh5a2.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1.r-htvplk.r-1udh08x > div > div > div.css-1dbjc4n.r-14lw9ot.r-6koalj.r-16y2uox.r-1wbh5a2 > div.css-1dbjc4n.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-1ye8kvj.r-13qz1uu > div > div > div > div:nth-child(6) > div'
    )

username.send_keys(Username)
next.click()
time.sleep(3)
password = driver.find_element(
    By.NAME,
    'password'
    )

password.send_keys(Password)

time.sleep(2)
login = driver.find_element(
    By.CLASS_NAME,
    'r-pw2am6')

login.click()
time.sleep(3)
tweet = driver.find_element(
    By.CLASS_NAME,
    'notranslate'
    )

tweet.send_keys(test.Report())

post = driver.find_element(
    By.XPATH,
    '//*[@id="react-root"]/div/div/div[2]/main/div/div/div/div/div/div[3]/div/div[2]/div[1]/div/div/div/div[2]/div[2]/div[2]/div/div/div[2]/div[3]'
)

post.click()