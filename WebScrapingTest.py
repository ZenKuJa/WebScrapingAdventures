import pdfkit

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


def main():
    driver = webdriver.Chrome()
    driver.get("http://training.kirchbergnet.de/t/index.php")
    assert "Kirchbergnet" in driver.title

    login_name = driver.find_element(By.NAME, "lid")
    kennwort = driver.find_element(By.NAME, "lkw")

    login_name.clear()
    login_name.send_keys("12345678")

    kennwort.clear()
    kennwort.send_keys("12345678")
    kennwort.send_keys(Keys.RETURN)

    assert "No results found." not in driver.page_source

    driver.get("http://training.kirchbergnet.de/t/training.php")

    db_systeme_fragen = driver.find_element(By.NAME, "befrage_2db")

    db_systeme_fragen.click()

    grundbegriffe = driver.find_element(By.NAME, "beliebig_gb")

    grundbegriffe.click()

    driver.execute_script("window.print()")

    driver.quit()
    ...

if __name__ == '__main__':
    main()