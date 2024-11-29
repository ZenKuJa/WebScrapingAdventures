class SubPage:
    title: str
    button_label: str
    last_page: int

    def __init__(self, title: str, button_label: str, last_page: int):
        self.title = title
        self.button_label = button_label
        self.last_page = last_page

    def get_title(self):
        return self.title

    def get_button_label(self):
        return self.button_label

    def get_last_page(self):
        return self.last_page