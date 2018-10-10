# Import af modulet PyPDF2, som bruges til at manipulere PDF dokumenter.
import PyPDF2
import pathlib
dir = '/home/byttemos/artikler/'
# definition af path hvorfra PDF'erne skal hentes
pathlist = pathlib.Path(dir).glob('**/*.pdf')
#print(pathlist)
#print(pathlib.Path)
list(pathlist)
for Path in pathlist:

# definition og åbning af dokument som pdfFileObj. Brug odfReader.XXXX til at lege med lortet. Her skal directory laves
# om til en variabel, så flere PDF'er kan itereres igennem koden. Desuden skal directory virke universelt, i stedet for kun på min maskine.
	pdfFileObj = open(pathlib.Path,'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)

# Outputter antallet af sider i PDF'en.
	print(pdfReader.numPages)
#	print(pathlist)

# Lukker dokumentet igen
	pdfFileObj.close()


	#VI SKAL BRUGE EN FUCKING ANDEN TING END EN GENERATOR (Str eller int)