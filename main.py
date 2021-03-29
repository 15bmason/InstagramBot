from selenium import webdriver
from time import sleep
import secret


class InstaBot:
    def __init__(self):
        self.driver = webdriver.Chrome("C:\\Users\\bluke\\Downloads\\chromedriver_win32 (1)\\chromedriver.exe")

    def spamSomeone(self, PN, PW, UN, MSG):
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
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(f"{UN}")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button").click()
        sleep(3)
        i = 0
        while(i < 5):
            print(MSG)
            sleep(0.5)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(f"{MSG}")
            sleep(0.5)
            self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
            i += 1
            MSG += MSG

    def singleMessage(self, PN, PW, UN, MSG):
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
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input").send_keys(f"{UN}")
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/nav/div[2]/div/div/div[2]/div[3]/div/div[2]/div/div[1]/a/div/div[2]/div[1]/div/div/div").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/main/div/header/section/div[1]/div[1]/div/div[1]/div/button").click()
        sleep(3)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea").send_keys(f"{MSG}")
        sleep(2)
        self.driver.find_element_by_xpath("/html/body/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[3]/button").click()
        sleep(2)

running = True
while running:
    answer = input("What would you like to do? ( Spam someone / Single message someone):  ").lower()
    try:
        if answer == "spam someone":
            person = input("Who would you like to spam? ( Edmund / Finlay / Ellie / Adam / Tom / Jack / Holly / Ethan / Harvey / Theo / Katie):  ").lower()
            gotPerson = secret.switch(person)
            spamContent = input("What would you like to spam?:  ").lower()
            spam = InstaBot()
            spam.spamSomeone(secret.PN, secret.PW, gotPerson, spamContent)
            running = False
        elif answer == "single message someone":
            person = input("Who would you like to message? ( Edmund / Finlay / Ellie / Adam / Tom / Jack / Holly / Ethan / Harvey / Theo / Katie):  ").lower()
            gotPerson = secret.switch(person)
            msgContent = input("What would you like to say?:  ").lower()
            msg = InstaBot()
            msg.singleMessage(secret.PN, secret.PW, gotPerson, msgContent)
            running = False
        else: 
            exit
    except:
        exit

        