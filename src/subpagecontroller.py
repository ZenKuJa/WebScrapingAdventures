import xml.etree.ElementTree as eTree
from src import subpage
from src.subpage import SubPage


class SubPageController:

    sub_pages: list[SubPage] = None

    def get_sub_pages(self):
        if self.sub_pages is None:
            self.sub_pages = []

            tree = eTree.parse(source="Data/sub_pages.xml")
            xml_sub_page = tree.findall(".//sub_page")

            for current_sub_page in xml_sub_page:
                title: str = current_sub_page.find("titel").text
                button_label: str = current_sub_page.find("button").text
                last_page: int = int(current_sub_page.find("pages").text)

                new_sub_page: SubPage = SubPage(title= title, button_label= button_label, last_page = last_page)
                self.sub_pages.append(new_sub_page)

        return self.sub_pages