from googletrans import Translator
from PyPDF2 import PdfReader

translator = Translator()

lista = ["orange", "apple", "love"]

# Traduzir textos

translations = translator.translate(lista, dest='pt')

for translation in translations:
    print(translation.text)

# Traduzir textos do pdf

reader = PdfReader("./PdfPython.pdf")
page = reader.pages[0]

for text in page.extract_text().split("\n"):
    print(translator.translate(text, dest='pt').text)