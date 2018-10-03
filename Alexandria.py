import PyPDF2

pdfFileObj = open('Multimodal literacy i klasserummet.pdf')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)

