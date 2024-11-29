from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from src.HtmlTextReader import HtmlTextReader
from src.PdfGenerator import PdfGenerator
from src.SubPageParser import SubPageParser
from src.WebPageTraverser import WebPageTraverser
from src.subpagecontroller import SubPageController


def main():

    need_updated_pages: bool = True

    if need_updated_pages:

        next_page_str: str = "next"
        solution_str: str ="pruefbut"

        driver = webdriver.Chrome()
        page_traverser = WebPageTraverser(driver = driver)

        page_traverser.login_page(
            url="http://training.kirchbergnet.de/t/index.php",
            username="12345678",
            password="12345678",
            uname_element="lid",
            pw_element="lkw")

        page_traverser.click_button_on_page(
            url="http://training.kirchbergnet.de/t/training.php",
            button_name="befrage_2db")

        #access sub_pages
        page_controller = SubPageController()
        sub_pages = page_controller.get_sub_pages()

        sub_page_parser = SubPageParser()
        sub_page_parser.extract_html_from_subpages(driver= driver, sub_pages= sub_pages, next_page_str= next_page_str, solution_str= solution_str)

        driver.quit()

    generate_pdf: bool = False

    if generate_pdf:
        txt_reader = HtmlTextReader()
        html_pages: list[str] = txt_reader.get_html_list_from_txt("Exports/html.txt")

        pdf_gen = PdfGenerator()
        pdf_gen.generate_pdf_from_html_list_selenium(html_pages)

if __name__ == '__main__':
    main()