from PyPDF2 import PdfReader
import pdfplumber

pdf_path = "Examen_endocrino.pdf"
output_file = "ankiexam.txt"

def extract_text_from_pdf(pdf_path):
    text = ""
    with open(pdf_path, "rb") as file:
        reader = PdfReader(file)
        num_pages = len(reader.pages)

        for page in range(num_pages):
            text += reader.pages[page].extract_text()

    return text

# Extraer texto del PDF
pdf_text = extract_text_from_pdf(pdf_path)

# Guardar el texto extraído en un archivo
with open(output_file, "w", encoding="utf-8") as file:
    file.write(pdf_text)

print("Extracción de texto completa. El archivo", output_file, "ha sido creado.")


pdf_path = "Examen_endocrino.pdf"

def extract_bold_text_from_pdf(pdf_path):
    bold_text = []
    with pdfplumber.open(pdf_path) as pdf:
        for page in pdf.pages:
            for obj in page.extract_words():
                if obj['font_size'] > 13:  # Ajusta este valor según tus necesidades
                    bold_text.append(obj['text'])

    return bold_text

bold_text_list = extract_bold_text_from_pdf(pdf_path)

# Imprimir el texto en negrita
for text in bold_text_list:
    print(text)