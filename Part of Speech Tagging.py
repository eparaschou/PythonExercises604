import nltk
sent1 = 'I am flying to Miami this weekend.'
tok1 = nltk.word_tokenize(sent1)
tagged_tok1 = nltk.pos_tag(tok1)
print (tagged_tok1)

sent2 = 'We are going to the game.'
tok2 = nltk.word_tokenize(sent2)
tagged_tok2 = nltk.pos_tag(tok2)
print (tagged_tok2)

sent3 = 'The kids are playing soccer.'
tok3 = nltk.word_tokenize(sent3)
tagged_tok3 = nltk.pos_tag(tok3)
print (tagged_tok3)

sent4 = 'He is teaching Finance.'
tok4 = nltk.word_tokenize(sent4)
tagged_tok4 = nltk.pos_tag(tok4)
print (tagged_tok4)

# abbreviations
#CC: conjunction, coordinating
#FW: foreign word
#IN: preposition or conjunction, subordinating
#JJ: adjective or numeral, ordinal
#NN: noun, common, singular or mass
#NNP: noun, proper, singular
#NNPS: noun, proper, plural
#NNS: noun, common, plural
#PRP: pronoun, personal
#RB: adverb
#VB: verb, base form
#VBD: verb, past tense