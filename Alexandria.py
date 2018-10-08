# Import af modulet PyPDF2, som bruges til at manipulere PDF dokumenter.
import PyPDF2
# definition og åbning af dokument som pdfFileObj. Brug odfReader.XXXX til at lege med lortet. Her skal directory laves
# om til en variabel, så flere PDF'er kan itereres igennem koden. Desuden skal directory virke universelt, i stedet for kun på min maskine.
pdfFileObj = open('/home/byttemos/Downloads/Biografisk metode.pdf' , 'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Outputter antallet af sider i PDF'en. Fjern hashtag for at inkludere den linje.

# print(pdfReader.numPages)


# Lukker dokumentet igen
pdfFileObj.close()
