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
	- Resources: [Natural Language Processing with Python](http://www.nltk.org/book/) Book
3. **Data Visualization** - Plot data as a two-axis chart. A script that reads the CSV file and outputs a two axis chart. 
	- Output: an image file with the chart correctly annotated.


Python Libraries
---

### Setup and Installation: 

[@katychuang](http://github.com/katychuang) prepared a requirements.txt file that you can use to install needed libraries with pip. To use this, create a virtual environment and run `pip install -r requirements.txt`.

### Note: 

In order to run the tokenizing script, you'll need to download the stop words copora from NLTK. You can do that with this command `python -c "import nltk; nltk.download()"`


Bibliography
---

* Karteek Addanki and Dekai Wu. 2013. Unsupervised rhyme scheme identification in hip hop lyrics using hidden markov models. In Proceedings of the First international conference on Statistical Language and Speech Processing (SLSP'13), Adrian-Horia Dediu, Carlos Martín-Vide, Ruslan Mitkov, and Bianca Truthe (Eds.). Springer-Verlag, Berlin, Heidelberg, 39-50. DOI=10.1007/978-3-642-39593-2_3 http://dx.doi.org/10.1007/978-3-642-39593-2_3 [PDF](http://www.cs.ust.hk/~dekai/library/WU_Dekai/AddankiWu_Slsp2013.pdf) [ACM Library](http://dl.acm.org/citation.cfm?id=2530107)
* Nakeisha Shannell Ferguson. 2008. [Bling-bling brand placements : measuring the effectiveness of brand mentions in hip-hop music](http://repositories.lib.utexas.edu/handle/2152/17959). Dissertation. UT Austin.
* Matt Garley and Julia Hockenmaier. 2012. Beefmoves: dissemination, diversity, and dynamics of English borrowings in a German hip hop forum. In *Proceedings of the 50th Annual Meeting of the Association for Computational Linguistics: Short Papers - Volume 2* (ACL '12), Vol. 2. Association for Computational Linguistics, Stroudsburg, PA, USA, 135-139. [PDF](http://www.aclweb.org/anthology/P12-2027) [ACM Library](http://dl.acm.org/citation.cfm?id=2390699)
* David Torres, Douglas Turnbull, Luke Barrington Gert Lanckriet. 2007. Identifying Words that are Musically Meaningful. In *ISMIR* Vol. 7, pp. 405-410. Chicago [PDF](http://cseweb.ucsd.edu/~datorres/bibs/MusicVocab_ISMIR07.pdf)

Reports
---

* [Product Mentions in Rap Music](http://www.uic.edu/orgs/kbc/hiphop/mentions.htm). (2003).

News Articles
---

* Stephen Armstrong. 2005. ['I'm drinkin' it - they payin' me for it'](http://www.theguardian.com/media/2005/jul/11/mondaymediasection.advertising). The Guardian.
* Susan Chandler. 2006. [Cristal unrapped: Or how most luxury-class products have learned to stop worrying and love the endorsement](http://articles.chicagotribune.com/2006-07-02/news/0607020255_1_hip-hop-artists-polaroid-cadillac). Chicago Tribune.
* Maya Grinberg. [Gold Diggers & Playa Haters: Mixed Responses to Hip Hop Marketing](http://cf.rims.org/Magazine/PrintTemplate.cfm?AID=3287)
* Gil Kaufman. 2003. [Push The Courvoisier: Are Rappers Paid For Product Placement?](http://www.mtv.com/news/1472393/push-the-courvoisier-are-rappers-paid-for-product-placement/)
* David Kiley. 2005. [Hip Hop Gets Down with the Deals](http://www.businessweek.com/stories/2005-05-15/hip-hop-gets-down-with-the-deals). Bloomberg Business Week. 
* David. A. Love. 2011. [Maybach's fall and the limits of rap product placement](http://thegrio.com/2011/11/30/does-hip-hop-product-placement-make-a-difference/). 
* Natalie Robehmed. [The Lyrical Portfolios Of Hip-Hop's Wealthiest Artists](http://www.forbes.com/sites/natalierobehmed/2014/04/16/the-lyrical-portfolios-of-hip-hops-wealthiest-artists/)

