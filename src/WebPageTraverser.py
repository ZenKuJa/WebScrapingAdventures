from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By


class WebPageTraverser:
    driver: webdriver

    def __init__(self, driver):
        self.driver = driver

    def login_page(self, url: str, username:str, password:str, uname_element: str, pw_element: str):
        self.driver.get(url)

        uname_element = self.driver.find_element(By.NAME, uname_element)
        pw_element = self.driver.find_element(By.NAME, pw_element)

        uname_element.clear()
        uname_element.send_keys(username)

        pw_element.clear()
        pw_element.send_keys(password)
        pw_element.send_keys(Keys.RETURN)

    def click_button_on_page(self, url: str, button_name: str):
        self.driver.get(url)

        button = self.driver.find_element(By.NAME, button_name)
        button.click()
    ...
