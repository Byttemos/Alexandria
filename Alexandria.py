import PyPDF2

pdfFileObj = open('~/hriskaer/Downloads/Multimodal literacy i klasserummet.pdf' , 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pdfFileObj.close()
