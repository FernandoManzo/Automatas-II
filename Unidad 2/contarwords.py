import os
import sys
import re
import time
import PyPDF2

def getPageCount(pdf_file):

	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pages = pdfReader.numPages
	return pages

def extractData(pdf_file, page):

	pdfFileObj = open(pdf_file, 'rb')
	pdfReader = PyPDF2.PdfFileReader(pdfFileObj)
	pageObj = pdfReader.getPage(page)
	data = pageObj.extractText()
	return data

def getWordCount(data):

	data=data.split()
	return len(data)

def main():
		# get the word count in the pdf file
		pdfFile = 'ArchivosCSV.pdf'
		totalWords = 0
		numPages = getPageCount(pdfFile)
		for i in range(numPages):
			text = extractData(pdfFile, i)
			totalWords+=getWordCount(text)
		time.sleep(1)

		print (totalWords)

if __name__ == '__main__':
	main()