#!/usr/bin/env python

""" This module parsing lyrics and counts brand mentions
"""

import nltk
import re
import codecs
import glob
import csv

__author__ = "Kat Chuang @katychuang"
__copyright__ = "Copyright 2014"
__credits__ = ["Kat Chuang"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Kat Chuang"
__email__ = "katychuang@gmail.com"
__status__ = "Development"


# Brands identified by Vanity Fair
brands = ["mercedes benz", "cristal", "lexus", "maybach", "bmw", "gucci", 
          "glock", "bentley", "nike", "range rover", "rolex", "porsche", 
          "versace", "tom ford", "intratec"]

csvOutput=[]


def openFile(lyricsfile, data=[]):
    with open(lyricsfile, 'rb') as textfile:
        stripped = (row for row in textfile if not row.startswith(('[')))
        data = [row for row in stripped if not len(row) == 0]

    return data

def tally(lines, song=""):    
    str1 = ''.join(lines)
    for product in brands:
        if str1.count(product) > 1:
            print "{}\t  {}x\t{}".format(product.strip(), str1.count(product), 
                                " ".join(song[7:-11].split("-")))

def tokenize(lines, normalize=False, song=""):
    str1 = ''.join(lines)

    tokens = nltk.word_tokenize(str1) # tokenizes the raw string
    text = nltk.Text(tokens)          # generate the text object

    sw = [",", "(", ")", "'"]

    if normalize:
        from nltk.corpus import stopwords

        stopwords = stopwords.words("english")
        more_stopwords = ["", "ass", ",", "fuck", "nigga", "niggas", "oh", "i", "'s", "bitches", "(", ")", ",", "i", "?",
        "!"]

        sw = more_stopwords + stopwords

    clean_text = ["".join(re.split("([.,;:!?`-])", word.lower())) for word in text if not word in sw]

    fdist = nltk.FreqDist(clean_text)
    return fdist

def writeFile(fdist, outputname, year, title):
    with codecs.open(outputname, 'w') as l:
        for word in fdist:
            temp = []
            if word in brands:
                l.write(word + "\t" + str(fdist[word]) + "\n") 

                temp.append(year)
                temp.append(title)
                temp.append(word)
                temp.append(fdist[word])
                
                if len(temp)>0: 
                    csvOutput.append(temp)

for song in glob.glob('lyrics/*.txt'):
    if "album-art" not in song:

        lines = openFile(song)

        print str(len(lines)) + " lines read from " + song

        fdist = tokenize(lines, False)
        # print "Distribution before normalization of stop words: ", str(len(fdist))
        output = song.replace("lyrics/", "frequencies/")
        writeFile(fdist, output, song[7:11], " ".join(song[12:-4].split("-")))

        fdistN = tokenize(lines, True)
        # print "Distribution after normalization of stop words: ", str(len(fdistN)), "\n"
        output = song.replace("lyrics/", "frequencies-normalized/")
        writeFile(fdistN, output, song[7:11], " ".join(song[12:-4].split("-")))



with open('frequencies.csv', 'wb') as csvfile:
    w = csv.writer(csvfile, delimiter=',')
    w.writerow(["year", "title", "brand", "mentions"])
    w.writerows(csvOutput)


# x = fdist.tabulate(samples=range(10), cumulative=True)



		

