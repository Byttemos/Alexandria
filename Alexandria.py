# Import af modulet PyPDF2, som bruges til at manipulere PDF dokumenter.
import PyPDF2
import pathlib
# definition af path hvorfra PDF'erne skal hentes
pathlist = path('/home/byttemos/artikler').glob('**/*.pdf')
for path in pathlist:

# definition og åbning af dokument som pdfFileObj. Brug odfReader.XXXX til at lege med lortet. Her skal directory laves
# om til en variabel, så flere PDF'er kan itereres igennem koden. Desuden skal directory virke universelt, i stedet for kun på min maskine.
pdfFileObj = open(path'rb')
pdfReader = PyPDF2.PdfFileReader(pdfFileObj)


# Outputter antallet af sider i PDF'en.
print(pdfReader.numPages)


# Lukker dokumentet igen
pdfFileObj.close()