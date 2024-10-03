#install nltk module
import nltk
import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

nltk.download()
# #once the download dialog opens - download book and popular packages
# #also download punkt from Models tab
# #and averaged_perception_tagger also from Model tab
from nltk.book import *
#

from nltk.book import *

print('name of the book = ', text1.name)
print ('length of book =', len(text1))


#to know what is UTF-8 look at lecture slides
my_file = open("shortstories.txt", "r", encoding="utf-8")
raw = my_file.read()
print (raw)

from nltk.book import text6, text3, text1

#let us search the text for every occurrence of a given word, together with some context.
print ("Showing all CONCORDANCE for a word")
text3.concordance('King')

# #find other words which appear in the same contexts as the specified word; list most similar words first
text6.similar('King')
print ('The Book of Genesis')
print ("\nShowing all words that are found in similar contxt as the given word\n")
text6.similar('Bridge')
# #
# #have some fun - allow nltk to build a paragraph from the text using words selected at random
print ("\nShowing paragraph from words selected by NLTK\n")
text6.generate()
# #
# #how a word is dispersed in the text
text3.dispersion_plot(['God'])