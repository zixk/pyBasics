import os
from PyPDF2 import PdfFileReader

def extract_information(pdf_path):
    with open(pdf_path,'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()
        metadata = pdf.getXmpMetadata()
    
    txt = f"""
    Information about {pdf_path}: 

    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information

if __name__ == "__main__":
    path = os.path.dirname(__file__)
    dirname = path + "/pdfs/sample1.pdf"
    extract_information(dirname)