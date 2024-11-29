import io
import os
import time

import img2pdf
import psutil
from PIL import Image

from PyPDF2 import PdfMerger, PdfWriter, PdfReader
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from weasyprint import HTML


class PdfGenerator:
    def __init__(self):
        ...

    def generate_pdf_from_html_list(self, html_pages: list[str]) -> None:

        content = "".join(html_pages)

        document = HTML(string=content).render()

        # document = HTML(string=html_pages[0]).render()
        #
        # for page in html_pages[1:]:
        #     document.append(HTML(string=page).render())

        document.write_pdf("DB_Aufgaben.pdf")


    def generate_pdf_from_html_list_selenium(self, html_pages: list[str]) -> None:
        chrome_options = Options()
        chrome_options.add_argument("--print-to-pdf")  # PDF-Druck aktivieren
        chrome_options.add_argument('--kiosk-printing')

        driver = webdriver.Chrome(options=chrome_options)

        driver.fullscreen_window()

        merger = PdfMerger()

        for i, page in enumerate(html_pages):

            print(f"{i+1}/{len(html_pages)}")

            # Temporäre HTML-Datei erstellen
            with open(f"Data/temp_{i}.html", "w") as f:
                f.write(page)

            # Seite im Browser öffnen
            driver.get(f"file:///{os.getcwd()}/Data/temp_{i}.html")


            # Warten, bis die Seite geladen ist (ggf. anpassen)
            driver.save_screenshot(f"Data/screenshot_{i}.png")

            screenshot = Image.open(f"Data/screenshot_{i}.png")

            # Bild in PDF konvertieren
            pdf_bytes = img2pdf.convert(screenshot.filename)

            # PDF-Reader und -Writer erstellen
            reader = PdfReader(io.BytesIO(pdf_bytes))
            writer = PdfWriter()
            writer.add_page(reader.pages[0])

            # PDF in Bytes schreiben
            with io.BytesIO() as temp_buffer:
                writer.write(temp_buffer)
                temp_buffer.seek(0)  # Cursor zurücksetzen

                # PDF aus Bytes lesen und an Merger anhängen
                merger.append(PdfReader(temp_buffer))

        driver.quit()

        with open("Exports/DB_Aufagben.pdf", "wb") as f:
            merger.write(f)

        for i in range(len(html_pages)):
            os.remove(f"Data/temp_{i}.html")
            os.remove(f"Data/screenshot_{i}.png")
