import nltk
#tokenizing a text file from your computer
import io

my_file = io.open("shortstories.txt", "r", encoding="utf-8")
raw = my_file.read()

import nltk

porter = nltk.PorterStemmer()
lancaster = nltk.LancasterStemmer()

#list1 = ['when', 'again', 'deeply', 'into', 'thrill']
porterlist1 = [porter.stem(t) for t in raw]
lancasterlist1 = [lancaster.stem(t) for t in raw]
print (porterlist1)
print (lancasterlist1)

#raw = """He was too much absorbed with his own thoughts to give any immediate
#answer to my remonstrance. He leaned upon his hand, with his untasted
#breakfast before him, and he stared at the slip of paper which he had
#just drawn from its envelope. Then he took the envelope itself, held it
#up to the light, and very carefully studied both the exterior and the
#flap."""
tokens = nltk.word_tokenize(raw)
print (tokens)

porterlist = [porter.stem(t) for t in tokens]
lancasterlist = [lancaster.stem(t) for t in tokens]

print (porterlist)
print (lancasterlist)

# text from nltk book is already tokenized so stemming won't work

# Tokenization = break down text into smaller units (tokens
# example: I am learning --> ["I", "am", "learning"]

# Stemming = reduce a word to its base or root form. Normaliza words to their base forms so that different variations of a word are treated as the same token. reduce dimensionality
# example: input = "running", "runner", "ran" --> stemming result = "run"

# Lemmatization = process of reducing a word to its base or dictionary form
# purpose: normalize words to their base forms while ensuring that the base form is a valid word
# it is more accurate than stemming
# example: input = "running", "runner", "ran" --> lemmatization -> "run"

