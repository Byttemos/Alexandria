# FUCK DEN HER SNOTKODE
import PyPDF2

pdfFileObj = open('/home/byttemos/Downloads/Biografisk metode.pdf' , 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
print(pdfReader.numPages)
pdfFileObj.close()
