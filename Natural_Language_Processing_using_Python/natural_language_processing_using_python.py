# -*- coding: utf-8 -*-
"""Natural Language Processing using Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1p4USTpFi0vgYe1DbSG1E8RjDG2wrqyUD
"""



import nltk
nltk.download('stopwords')

import urllib.request
response =  urllib.request.urlopen('https://en.wikipedia.org/wiki/SpaceX')
html = response.read()
html

html

from bs4 import BeautifulSoup
soup = BeautifulSoup(html,'html5lib')
text = soup.get_text(strip = True)
print(text)

tokens = [t for t in text.split()]
print(tokens)

# Iterating over the text
#for token in tokens:
 #  print(token.tokens)

"""##Count word Frequency
nltk offers a function FreqDist() which will do the job for us. Also, we will remove stop words (a, at, the, for etc) from our web page as we don't need them to hamper our word frequency count.
"""

from nltk.corpus import stopwords
sr= stopwords.words('english')
clean_tokens = tokens[:]
for token in tokens:
    if token in stopwords.words('english'):
        
        clean_tokens.remove(token)
freq = nltk.FreqDist(clean_tokens)
for key,val in freq.items():
    print(str(key) + ':' + str(val))
freq.plot(20, cumulative=False)
