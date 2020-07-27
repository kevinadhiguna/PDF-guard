from PyPDF2 import PdfFileWriter, PdfFileReader

pdfWriter = PdfFileWriter()

# Read the pdf file which will be encrypted
pdf = PdfFileReader("example.pdf")

for page_num in range(pdf.numPages):
    pdfWriter.addPage(pdf.getPage(page_num))

# Encryption process goes here
passw = input('Enter your password: ')
pdfWriter.encrypt(passw)
print('Password was set successfully !')

setNewName = input('What will you name your encrypted pdf? (without ".pdf") : ')
newPdfName = str(setNewName) + '.pdf'

# Create a new encrypted PDF
with open(newPdfName, 'wb') as f:
    pdfWriter.write(f)
    f.close()

print('Excellent! You have secured your PDF file!')
