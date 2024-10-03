
# normal python in built function

str1 = '''This chapter is divided into sections that skip between two quite different styles. 
In the "computing with language" sections we will take on some linguistically motivated 
programming tasks without necessarily explaining how they work. 
In the "closer look at Python" sections we will systematically review key programming 
concepts. We'll flag the two styles in the section titles, but later chapters 
will mix both styles without being so up-front about it. We hope this style of 
introduction gives you an authentic taste of what will come later,
while covering a range of elementary concepts in linguistics and computer science. 
If you have basic familiarity with both areas, you can skip to 5; we will repeat 
any important points in later chapters, and if you miss anything you can easily 
consult the online reference material at http://nltk.org/. If the material is 
completely new to you, this chapter will raise more questions than it answers, 
questions that are addressed in the rest of this book.'''
findinstr = str1.find('book')
print ("first occurence of the substring", findinstr)
print (str1[findinstr:findinstr+4])


#convert the string into a sorted list using the default delimiter - space
list1 = (str1.split())
#print (list1)
#try to find all occurences of a specific word
indices = [i for i, x in enumerate(list1) if x == "you"]
print (indices)