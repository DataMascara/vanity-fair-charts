# Module for parsing lyrics and counting brand mentions


import nltk
import re
import codecs

lyricsfile = "lyrics/2013-tom-ford-lyrics.txt"

def openFile(lyricsfile, data=[]):
    with open(lyricsfile, 'rb') as textfile:
        stripped = (row.strip() for row in textfile if not row.startswith(('[')))
        data = [row for row in stripped if not row == ""]

    return data


raw = openFile(lyricsfile) 


