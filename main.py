# Traduzir palavras e textos em documentos PDF

# requisitos
# vscode
# python
# pip install googletrans==3.1.0a0
# pip install PyPDF2

# Contexto de uso:
# googletrans
# Tradução de textos
# Melhoria da acessibilidade
# PyPDF2
# Extração, processamento, análise e visualização de dados em documentos PDF

from googletrans import Translator
from PyPDF2 import PdfReader

translator = Translator()

lista = ["orange", "apple", "love"]

translations = translator.translate(lista, dest='pt')

for translation in translations:
    print(translation.text)

# Traduzir textos do pdf

reader = PdfReader("./PdfPython.pdf")
page = reader.pages[0]

for text in page.extract_text().split("\n"):
    print(translator.translate(text, dest='pt').text)