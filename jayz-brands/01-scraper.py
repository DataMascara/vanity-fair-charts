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



root = "http://genius.com"

albums = [
["1996", "Reasonable Doubt", "/albums/Jay-z/Reasonable-doubt"], 
["1997", "In My Lifetime", "/albums/Jay-z/In-my-lifetime-vol-1"],
["1998", "Vol 2... Hard Knock Life", "/albums/Jay-z/Vol-2-hard-knock-life"],
["1999", "Vol 3... Life and Times of S. Carter", "/albums/Jay-z/Vol-3-life-and-times-of-s-carter"],
["2000", "The Dynasty: Roc La Familia", "/albums/Jay-z/The-dynasty-roc-la-familia"],
["2001", "The Blueprint", "/albums/Jay-z/The-blueprint"], 
["2002", "The Best of Both Worlds", "/albums/Jay-z/The-best-of-both-worlds"],
["2002", "Blueprint 2", "/albums/Jay-z/The-blueprint-2-the-gift-the-curse"],
["2003", "The Black Album", "/albums/Jay-z/The-black-album"],
["2004", "Unfinished Business", "/albums/Jay-z/Unfinished-business"],
["2006", "Kingdom Come", "/albums/Jay-z/Kingdom-come"],
["2007", "American Gangster", "/albums/Jay-z/American-gangster"], 
["2009", "The Blueprint 3", "/albums/Jay-z/The-blueprint-3"],
["2011", "Watch the Throne", "/albums/Kanye-west/Watch-the-throne"],
["2013", "Magna Carta... Holy Grail", "/albums/Jay-z/Magna-carta-holy-grail"],
]

# download lyrics from each album
def songLyrics(year, page):

    # load downloaded page into BS
    html = BeautifulSoup(page.text)
    song_links = []

    # grab all the links in .song_list elements
    song_links.extend((a['href'] for a in html.select(".song_list li a")))
     
    songs = list(set(song_links))

    for song in songs:
        lyrics = [] # start with empty list
        
        if "album-art" not in song:
            # make a request to grab each page linked to
            page = requests.get(root+song)
            outputname = "lyrics/" + year + song[6:] + ".txt"
            print outputname

            html = BeautifulSoup(page.text)
            # the div with the content we want has the class "lyrics"
            lines = html.select(".lyrics")
            pebble = []
            
            for line in lines:
                [a.unwrap() for a in line.select("a")]
                [br.unwrap() for br in line.select("br")]
                pebble.append(line)

            lyrics.extend(pebble) # save it all into lyrics list
            
            with codecs.open(outputname, 'w', 'utf-8') as l:
              [l.write(lyric.get_text()) for lyric in lyrics]
            
        

# go through list of albums and grab page
for album in albums:
    year = album[0]
    path = album[2]
    page = requests.get(root+path)
    songLyrics(year, page)

# ------
# Credits to @jiko's example https://gist.github.com/jiko/7305816

