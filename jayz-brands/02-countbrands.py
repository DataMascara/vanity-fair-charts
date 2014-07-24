# Module for parsing lyrics and counting brand mentions


import nltk
import re
import codecs

lyricsfile = "lyrics/2013-tom-ford-lyrics.txt"

def openFile(lyricsfile, data=[]):
    with open(lyricsfile, 'rb') as textfile:
        stripped = (row for row in textfile if not row.startswith(('[')))
        data = [row for row in stripped if not len(row) == 0]
    return data

def tokenize(lines):
	str1 = ''.join(lines)
	tokens = nltk.word_tokenize(str1) # tokenizes the raw string
	text = nltk.Text(tokens)          # generate the text object
	clean_text = ["".join(re.split("([.,;:!?'`-])", word)) for word in text]
	fdist = nltk.FreqDist(clean_text)
	return fdist

def writeFile(fdist):
	outputname = "frequencies/2013-tom-ford-lyrics.txt"
	with codecs.open(outputname, 'w', 'utf-8') as l:
		[l.write(word + "\t\t\t" + str(fdist[word]) + "\n") for word in fdist]

lines = openFile(lyricsfile) 
fdist = tokenize(lines)

print "Distribution before normalization of stop words\n", fdist, "\n"
writeFile(fdist)

