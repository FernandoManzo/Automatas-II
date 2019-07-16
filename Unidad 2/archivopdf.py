import PyPDF2
import itertools

#pdf_file = open('ArchivosCSV.pdf', 'rb')
#read_pdf = PyPDF2.PdfFileReader(pdf_file)

#Contamos las paginas
#number_of_pages = read_pdf.getNumPages()
#print(number_of_pages)

#pdf_file.close()

# cuenta-elementos-de-lista-1.py

pdf_file = open('ArchivosCSV.pdf', 'rb')
read_pdf = PyPDF2.PdfFileReader(pdf_file)

#cadenaPalabras = 'it was the best of. Times it was the worst of times '
#cadenaPalabras += 'it was the, age of wisdom it was the age of foolishness'

listaPalabras = read_pdf.split()

frecuenciaPalab = []
for w in listaPalabras:
    frecuenciaPalab.append(listaPalabras.count(w))

print("Cadena\n" + cadenaPalabras +"\n")
print("Lista\n" + str(listaPalabras) + "\n")
print("Frecuencias\n" + str(frecuenciaPalab) + "\n")
print("Pares\n" + str(zip(listaPalabras, frecuenciaPalab)))

pdf_file.close()

