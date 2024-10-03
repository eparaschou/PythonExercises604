import nltk
from nltk.corpus import wordnet

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()
wnl = nltk.WordNetLemmatizer()

list1 = ['crying', 'cried', 'cries', 'cry']

porterlist1 = [porter.stem(t) for t in list1]
lancasterlist1 = [lancaster.stem(t) for t in list1]
wnllist1 = [wnl.lemmatize(t) for t in list1]

print (porterlist1)
print (lancasterlist1)
print (wnllist1)

raw = """He was too much absorbed with his own thoughts to give any immediate
answer to my remonstrance. He leaned upon his hand, with his untasted
breakfast before him, and he stared at the slip of paper which he had
just drawn from its envelope. Then he took the envelope itself, held it
up to the light, and very carefully studied both the exterior and the
flap."""
tokens = nltk.word_tokenize(raw)

porterlist = [porter.stem(t) for t in tokens]
lancasterlist = [lancaster.stem(t) for t in tokens]
wnllist = [wnl.lemmatize(t) for t in tokens]

print (porterlist)
print (lancasterlist)
print (wnllist)