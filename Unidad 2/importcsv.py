import csv
import itertools

#f = open("datos.txt")
#f = opena("truncate.txt")
#x = f.readlines()
#s = []

#for i in x:
#	i = i.replace(",","")
#	j = i.replace("",",")
#	s.append(j)

#csvex = csv.writer(open("datosc.txt", "w"), delimiter=',',quoting=csv.QUOTE_ALL)
#csvex.writerow(s)


#with open('datos.txt', 'r') as in_file:
#    stripped = (line.strip() for line in in_file)
#    lines = (line.split(",") for line in stripped if line)
#    with open('datos.csv', 'w') as out_file:
#        writer = csv.writer(out_file)
#        writer.writerow(('Columna1', 'Columna2', 'Columna3', 'Columna4', 'Columna5'))
#        writer.writerows(lines)


#with open('datos.txt', 'r') as in_file:
#    lines = in_file.read().splitlines()
#    stripped = [line.replace(","," ").split() for line in lines]
#    grouped = zip(*[stripped]*1)
#    with open('datos.csv', 'w') as out_file:
#        writer = csv.writer(out_file)
#        writer.writerow(('Columna1', 'Columna2', 'Columna3'))
#        for group in grouped:
#            writer.writerows(group)

#import os.path
#import csv
 
#save_path = "C:/Users/f3r_c/Documents/Automatas II/Unidad 2/"
 
#completeName_in  = os.path.join(save_path,'datos'+'.txt')
#completeName_out = os.path.join(save_path,'datos'+'.csv')
 
  
#file1=open(completeName_in)
#In_text = csv.reader(file1,delimiter = ',')
 
#file2 =open(completeName_out,'w')
#out_csv = csv.writer(file2)
 
#file3 = out_csv.writerows(In_text)
 
#file1.close()
#file2.close()

# Open the txt file
file = open("datos.txt", 'r', encoding = "utf-8")

# Read the file
new_text = file.readlines()

# Create a list to keep all the words in file
words = []
line_break = 0

# Add all the words in file to list
for x in range(0, len(new_text)):
	for word in new_text[x].split():
		words.append(word + ',')

# Write words into csv file
f = open('datos.csv','w')
for x in range(0, len(words)):
	if (line_break == 5):
		f.write('\n')
		f.write(words[x])
		line_break = 1
	else:
		f.write(words[x])
		line_break += 1
f.close()