from io import TextIOWrapper


class HtmlTextReader:

    def __init__(self):
        ...

    def get_html_list_from_txt(self, text_path: str) -> list[str]:
        txt_file = open(text_path, "r")
        content: str = txt_file.read()

    #<html><head>
    #< / body > < / html >



    ...