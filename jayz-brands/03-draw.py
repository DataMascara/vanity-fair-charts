#!/usr/bin/env python

""" This module takes the csv files and charts data
"""


import matplotlib.pyplot as plt; plt.rcdefaults()
import numpy as np
import matplotlib.pyplot as plt
import csv
import glob
from pylab import *

brands = ["mercedes benz", "cristal", "lexus", "maybach", "bmw", "gucci", 
          "glock", "bentley", "nike", "range rover", "rolex", "porsche", 
          "versace", "tom ford", "intratec"]

def d(x, y, f, i):
    y_pos = np.arange(len(x))
    error = np.random.rand(len(x))

    plt.barh(y_pos, y, xerr=error, align='center', alpha=0.4)
    plt.yticks(y_pos, x)
    plt.xlabel('Occurrence')
    plt.title('Brands mentioned in ')
    plt.show()
    
def openFile(lyricsfile, i):
    x=[]
    y=[]
    yyyy=""

    with open(lyricsfile, 'r') as textfile:
        reader = csv.reader(textfile, delimiter='\t')
        for brand, mentions in reader:
            if brand in brands:
                x.append(brand)
                y.append(int(mentions))


    # year.append(lyricsfile[23:27])
    print "{}\t{} brands identified".format(lyricsfile[23:], len(x))
    if len(x)>0:    
        d(x, y, lyricsfile, i)

songs = glob.glob('frequencies-normalized/*.txt')
for song in songs:
    if "album-art" not in song:
        lines = openFile(song, songs.index(song))


