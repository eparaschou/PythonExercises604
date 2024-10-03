import nltk
from nltk.corpus import wordnet
import io

my_file = io.open("shortstories.txt", "r", encoding="utf-8")
raw = my_file.read()

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
wnl = nltk.WordNetLemmatizer()

porterlist1 = [porter.stem(t) for t in raw]
lancasterlist1 = [lancaster.stem(t) for t in raw]
wnllist1 = [wnl.lemmatize(t) for t in raw]
print (porterlist1)
print (lancasterlist1)
print (wnllist1)

tokens = nltk.word_tokenize(raw)

porterlist = [porter.stem(t) for t in tokens]
lancasterlist = [lancaster.stem(t) for t in tokens]
wnllist = [wnl.lemmatize(t) for t in tokens]

print (porterlist)
print (lancasterlist)
print (wnllist)