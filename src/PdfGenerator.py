import io
import os

import warnings

import img2pdf
import pdfkit
from PIL import Image
from pypdf import PdfWriter, PdfReader, PdfMerger

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from weasyprint import HTML


class PdfGenerator:
    def __init__(self):
        ...

    def generate_pdf_from_html_list_pypdf(self, html_pages: list[str]) -> None:

        merger = PdfWriter()

        config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

        options = {
            'no-images': ''
        }

        for i, page in enumerate(html_pages):
            print(f"{i + 1}/{len(html_pages)}")

            # Temporäre HTML-Datei erstellen
            with open(f"Data/temp_{i}.html", "w") as f:
                f.write(page)

            pdfkit.from_file(f"Data/temp_{i}.html", f"Data/temp_{i}.pdf", configuration=config, options=options)

            merger.append(f"Data/temp_{i}.pdf")

        merger.write("Exports/DB_Aufagben_new.pdf")

        for i in range(len(html_pages)):
            os.remove(f"Data/temp_{i}.html")
            os.remove(f"Data/temp_{i}.pdf")
        ...