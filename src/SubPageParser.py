from src.subpage import SubPage
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.HtmlTextReader import HtmlTextReader
from src.PdfGenerator import PdfGenerator
from src.subpagecontroller import SubPageController

class SubPageParser:

    def extract_html_from_subpages(self,driver: webdriver,  sub_pages: list[SubPage], next_page_str: str, solution_str: str) -> None:

        html_pages = [str]

        for sub_page in sub_pages:
            chapter_button = driver.find_element(By.NAME, sub_page.get_button_label())
            chapter_button.click()
            print(f"~~~~~~~~~~ {sub_page.get_button_label()} ~~~~~~~~~~")
            for i in range(sub_page.get_last_page()):
                print(f"currently at subpage: {i+1}/{sub_page.get_last_page()}")

                next_page_button = driver.find_element(By.NAME, next_page_str)
                solution_button = driver.find_element(By.ID, solution_str)
                solution_button.click()
                html_pages.append(driver.page_source)
                next_page_button.click()

            driver.get("http://training.kirchbergnet.de/t/training.php")
            db_systeme_fragen = driver.find_element(By.NAME, "befrage_2db")
            db_systeme_fragen.click()

        with open("Exports/html.txt", "w") as datei:
            pass

        with open("Exports/html.txt", "a", encoding="utf-8") as datei:
            for html_str in html_pages:
                datei.write(f"\n{html_str}\n")