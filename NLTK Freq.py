import nltk
from nltk.book import text2

#use the freqDist fucntion in nltk to obtain the frequencey distribution
text2_freqdist = nltk.FreqDist(text2)
print (text2_freqdist,'\n')
# #
# # #or print it in a tabulated format
text2_freqdist.tabulate()
#
#now find the 10 most common words in the text
most_common = (text2_freqdist.most_common(100))
print (most_common,'\n')
# #
# # #what about words that occur only once - such words are known as hapaxes
hapax = text2_freqdist.hapaxes()
print ('The hapaxes in the text are: ', hapax)


# #how many times do the two protagonists appear in the book
moby = text2_freqdist['Moby']
ahab = text2_freqdist['Ahab']
print ('Number of time Moby occurs: ', moby, 'and Number of times Ahab occurs: ',ahab)
# #
# #which are the longest words in this text
text2_set = set(text2) #first order the text so it removes the duplicates
# print (text1_set)
long_words = [w for w in text2_set if len(w) > 15]
print ('Number of long words is: ',len(long_words), sorted(long_words))

common = []
for i in hapax:
    if i in long_words:
        common.append(i)
print ("common to hapax and long are:", common)
#words that occur together
print ('COLLOCATIONS in the text are:')
text2.collocations()
