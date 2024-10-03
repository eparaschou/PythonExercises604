import nltk
#tokenizing a text file from your computer
import io

my_file = io.open("shortstories.txt", "r", encoding="utf-8")
raw = my_file.read()

# #tokenize the content at the word level
# Tokenizes the content of raw into individual words (tokens).
tokens = nltk.word_tokenize(raw)
# print ("Tokens are: ", tokens)

# #tokenize the content at the sentence level
#sent_tokens = nltk.sent_tokenize(raw)
#print ("Sentence tokens are", sent_tokens)
#
# #convert the tokens into a text object which we can then use for our analysis
#This is a text object similar to what you got from the NLTK books
my_text_obj = nltk.Text(tokens)
# #
# # ##Now you can run all the same code that analyzes the text
# # #use the freqDist fucntion in nltk to obtain the frequencey distribution
text1_freqdist = nltk.FreqDist(my_text_obj)
# #print (text1_freqdist)
# #or print it in a tabulated format
# #text1_freqdist.tabulate()
#
# #now find the 50 most common words in the text
most_common = (text1_freqdist.most_common(50))
print (most_common)
#
#what about words that occur only once - such words are known as hapaxes
hapax = text1_freqdist.hapaxes()
print ('The hapaxes in the text are: ', hapax)

#find collocations
my_text_obj.collocations()