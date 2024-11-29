from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from GeneratePdfFromHTML import GeneratePdfFromHTML
from src.subpagecontroller import SubPageController

def main():
    #
    # next_page_str: str = "next"
    # solution_str: str ="pruefbut"
    #
    # #Page-Login
    # driver = webdriver.Chrome()
    # driver.get("http://training.kirchbergnet.de/t/index.php")
    #
    # assert "Kirchbergnet" in driver.title
    #
    # login_name = driver.find_element(By.NAME, "lid")
    # kennwort = driver.find_element(By.NAME, "lkw")
    #
    # login_name.clear()
    # login_name.send_keys("12345678")
    #
    # kennwort.clear()
    # kennwort.send_keys("12345678")
    # kennwort.send_keys(Keys.RETURN)
    #
    # assert "No results found." not in driver.page_source
    #
    # #navigate to db_exercises
    # driver.get("http://training.kirchbergnet.de/t/training.php")
    # db_systeme_fragen = driver.find_element(By.NAME, "befrage_2db")
    # db_systeme_fragen.click()
    #
    # #access sub_pages
    # page_controller = SubPageController()
    # sub_pages = page_controller.get_sub_pages()
    #
    # html_pages = [str]
    #
    # for sub_page in sub_pages:
    #     chapter_button = driver.find_element(By.NAME, sub_page.get_button_label())
    #     chapter_button.click()
    #     print(f"~~~~~~~~~~ {sub_page.get_button_label()} ~~~~~~~~~~")
    #     for i in range(sub_page.get_last_page()):
    #         print(f"currently at subpage: {i}/{sub_page.get_last_page()}")
    #
    #         next_page_button = driver.find_element(By.NAME, next_page_str)
    #         solution_button = driver.find_element(By.ID, solution_str)
    #         solution_button.click()
    #         html_pages.append(driver.page_source)
    #         next_page_button.click()
    #
    #     driver.get("http://training.kirchbergnet.de/t/training.php")
    #     db_systeme_fragen = driver.find_element(By.NAME, "befrage_2db")
    #     db_systeme_fragen.click()
    #
    # with open("Exports/html.txt", "w") as datei:
    #     pass
    #
    # with open("Exports/html.txt", "a", encoding="utf-8") as datei:
    #     for html_str in html_pages:
    #         datei.write(f"\n{html_str}\n")

    pdf_gen = GeneratePdfFromHTML()

    pdf_gen.generate_pdf()









if __name__ == '__main__':
    main()