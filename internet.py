from selenium import webdriver
from selenium.webdriver.common.by import By
import time


class intern():

    def __init__(self):
        self.site = 'https://fast.com/'
        self.options = webdriver.ChromeOptions()
        self.options.add_experimental_option('detach', True)
        self.driver = webdriver.Chrome(options=self.options)
        self.driver.get(self.site)
        time.sleep(15)
        self.more = self.driver.find_element(
            By.CLASS_NAME,
            'more-info-link'
        )
        self.more.click()
        time.sleep(15)

        self.down_speed = self.driver.find_element(
            By.ID,
            'speed-value'
        ).text

        self.up_speed = self.driver.find_element(
            By.ID,
            'upload-value'
        ).text
        time.sleep(5)
        self.driver.quit()

    def Report(self):
        return f"Your Internet Speed is {self.down_speed}mbps with upload speed of {self.up_speed}mbps.\n\nTest down at www.fast.com"


