from io import TextIOWrapper


class HtmlTextReader:

    def __init__(self):
        ...

    def get_html_list_from_txt(self, text_path: str) -> list[str]:
        return_list = []

        txt_file = open(text_path, "r")
        content: str = txt_file.read()

        start_tag: str = "<html><head>"
        end_tag: str = "</body></html>"

        index_start: int = 0
        index_end: int = 0

        while index_start != -1 and index_end != -1:
            index_start = content.find(start_tag)
            index_end = content.find(end_tag) + len(end_tag)

            new_html_page: str = content[index_start:index_end]


            new_html_page = self.remove_html_Tag(new_html_page, "script")

            return_list.append(new_html_page)

            content = content[index_end:]

        return return_list

    def remove_html_Tag(self, html_str: str, tag: str) -> str:

        new_html_str: str = html_str

        start_tag: str = f"<{tag}>"
        end_tag: str = f"</{tag}>"


        for i in range(int(html_str.count(tag)/2)):
            index_start = new_html_str.find(start_tag) - len(start_tag)
            index_end = new_html_str.find(end_tag) + len(end_tag)

            new_html_str = new_html_str[:index_start] + new_html_str[index_end:]

        return new_html_str
