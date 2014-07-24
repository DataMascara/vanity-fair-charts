# Module for parsing lyrics and counting brand mentions


import nltk
import re
import codecs


brands = ["Mercedes Benz", "Cristal", "Lexus", "Maybach", "BMW", "Gucci", "Glock", "Bentley", "Nike",
"Range Rover", "Rolex", "Porsche", "Versace", "Tom Ford", "Intratec"]

def openFile(lyricsfile, data=[]):
    with open(lyricsfile, 'rb') as textfile:
        stripped = (row for row in textfile if not row.startswith(('[')))
        data = [row for row in stripped if not len(row) == 0]
    return data

def tokenize(lines, normalize=False):
	str1 = ''.join(lines)
	tokens = nltk.word_tokenize(str1) # tokenizes the raw string
	text = nltk.Text(tokens)          # generate the text object

	sw = [",", "(", ")", "'"]

	if normalize:
		from nltk.corpus import stopwords

		stopwords = stopwords.words("english")
		more_stopwords = ["", "ass", ",", "fuck", "nigga", "niggas", "oh", "i", "'s"]

		sw = more_stopwords + stopwords
	
	clean_text = ["".join(re.split("([.,;:!?`-])", word.lower())) for word in text if not word  in sw]
	
	fdist = nltk.FreqDist(clean_text)
	return fdist

def writeFile(fdist, outputname):
	with codecs.open(outputname, 'w', 'utf-8') as l:
		[l.write(word + "\t\t\t" + str(fdist[word]) + "\n") for word in fdist]




lyricsfile = "lyrics/2013-tom-ford-lyrics.txt"
lines = openFile(lyricsfile) 
fdist = tokenize(lines, False)

print "Distribution before normalization of stop words\n", fdist, " ", str(len(fdist)), "\n"
writeFile(fdist, "frequencies/2013-tom-ford-lyrics.txt")

fdistN = tokenize(lines, True)

print "Distribution after normalization of stop words\n", fdistN, " ", str(len(fdistN))
writeFile(fdistN, "frequencies/2013-tom-ford-lyrics-normalized.txt")



# x = fdist.tabulate(samples=range(10), cumulative=True)



		

