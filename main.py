from selenium import webdriver
from time import sleep
import secret


class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Users\\bluke\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

    def spamEddie(self, PN, PW):
        self.driver.get("https://instagram.com")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[2]/div/div/div/div[2]/button[1]").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/article/div[2]/div[1]/div/form/div/div[5]/button/span[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[3]/div[2]/div/div/div/div/div[3]/button[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[1]/input").send_keys(PN)
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[2]/input").send_keys(PW)
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/div[3]/div[1]/div/div/div[2]/div[1]/form/div/div[3]/button").click()
        sleep(12)
        try:
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        except:
            sleep(12)
            self.driver.find_element_by_xpath("/html/body/div[4]/div/div/div/div[3]/button[2]").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys("_richardson.edmund_")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button").click()
        sleep(3)
        i = 0
        while(i < 5):
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys("Tom Millard is a tiny human being")
            sleep(2)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
            sleep(2)
            i += 1

my_bot = InstaBot()
my_bot.spamEddie(secret.PN, secret.PW)