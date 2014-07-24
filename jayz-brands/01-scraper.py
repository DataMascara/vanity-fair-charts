#!/usr/bin/env python

""" This module downloads a list of lyrics from RapGenius
"""


import requests # for grabbing pages
from bs4 import BeautifulSoup # for parsing pages
import codecs


__author__ = "Kat Chuang @katychuang"
__copyright__ = "Copyright 2014"
__credits__ = ["Kat Chuang"]
__license__ = "GPL"
__version__ = "0.0.1"
__maintainer__ = "Kat Chuang"
__email__ = "katychuang@gmail.com"
__status__ = "Development"


 
# grab page
root = "http://rapgenius.com"
path = "/albums/Jay-z/American-gangster"
page = requests.get(root+path)
year = "2007"
 
# load downloaded page into BS
html = BeautifulSoup(page.text)
song_links = []
# let's grab all the links in .song_list elements
song_links.extend((a['href'] for a in html.select(".song_list li a")))
 
songs = list(set(song_links))
lyrics = []
for song in songs:
    
    # make a request to grab each page linked to
    page = requests.get(root+song)
    outputname = "lyrics/" + year + song[6:] + ".txt"
    print outputname
    html = BeautifulSoup(page.text)
    # the div with the content we want has the class "lyrics"
    lines = html.select(".lyrics")
    pebble = []
    
    for line in lines:
        # discard all the tags but save their content
        [a.unwrap() for a in line.select("a")]
        [br.unwrap() for br in line.select("br")]
        pebble.append(line)
        # section it out by [*]
        # if the [*] has no artist name (indicated by a colon) or the artist name "2 Chainz"
        # we want those lyrics
        # otherwise, discard
    lyrics.extend(pebble) # save it all into lyrics list
    
    with codecs.open(outputname, 'w', 'utf-8') as l:
      [l.write(lyric.get_text()) for lyric in lyrics]
    
    lyrics = [] # clear it after each file

# ------
# Credits to @jiko's example https://gist.github.com/jiko/7305816
