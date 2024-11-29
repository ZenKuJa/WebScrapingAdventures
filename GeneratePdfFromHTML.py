import pdfkit


class GeneratePdfFromHTML:
    def __init__(self):
        ...

    def generate_pdf(self) -> None:
        with open("Exports/html.txt", "r", encoding="utf-8") as datei:
            inhalt = datei.read()

        html_code = f"""
        <!DOCTYPE html>
        <html>
        <head>
          <meta charset="utf-8">
        </head>
        <body>
            {inhalt}
        </body>
        </html>
        """

        pdfkit.from_string(html_code, "Aufgaben.pdf")
        ...