Objective
---

We're going to recreate this chart: 
![](original.jpg)

**Source:** This was first published by Vanity Fair in October 2013. ([source](http://www.vanityfair.com/hollywood/2013/10/jay-z-brands-song-chart))

Steps Involved
---

1. **Data collection** - Create a scraper for downloading lyrics for each album. This should only take 1 python file that contains that downloads lyrics from RapGenius.
	- Output:  A directory named 'lyrics' that contains text files. Each file will be named with year then title. For example, `2007-Hello-Brooklyn.txt`.
2. **Data analysis** - Tokenize words and count each mention of a brand name. This should be 1 python file that reads the lyric text files and outputs a comma separated file described below.
	- Output: A comma separated file (CSV) that contains three columns: year, brand, frequency.
3. **Data Visualization** - Plot data as a two-axis chart. A script that reads the CSV file and outputs a two axis chart. 
	- Output: an image file with the chart correctly annotated.


Python Libraries
---

Setup: [@katychuang](http://github.com/katychuang) prepared a requirements.txt file that you can use to install needed libraries with pip. To use this, create a virtual environment and run `pip install -r requirements.txt`.

Note: In order to run the tokenizing script, you'll need to download the stop words copora from NLTK. You can do that with this command `python -c "import nltk; nltk.download()"`


