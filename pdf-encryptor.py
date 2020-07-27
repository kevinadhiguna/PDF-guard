from PyPDF2 import PdfFileWriter, PdfFileReader

pdfWriter = PdfFileWriter()

# Read the pdf file which will be encrypted
pdf = PdfFileReader("example.pdf")

for page_num in range(pdf.numPages):
    pdfWriter.addPage(pdf.getPage(page_num))

# Encryption process goes here
passw = "12345"
pdfWriter.encrypt(passw)

# Create a new encrypted PDF
with open("encrypted.pdf", 'wb') as f:
    pdfWriter.write(f)
    f.close()
