dict1 = {"num1": "Donald", "num2":"Mickey","num3":"Bugs",
         "num4":"Daffy"}
dict2 = {1:1223, 2:234,3:345,"a":123}

print(dict1["num1"])
print(dict1["num2"])
print(dict2[3])
print(dict2['a'])
print(len(dict1))

# the order inside the dictionary doesn't matter
# it is not zero based; can access any value using its key
# it is a mutable collection like a list

class_roster = {101:'jay',102:'andy',
                103:'robert', 104:'emma'}
roll_1 = class_roster[101]
dict_of_squares = {}
for i in range(10):
    # add a key to the dictionary with the value i
    # for the value of that key is the square of i
    dict_of_squares[i] = i**2
print(dict_of_squares)

print(len(dict_of_squares))
del (dict_of_squares[5])
print(dict_of_squares)

# create a dictionary of numbers and their cubes between 1 to 100 that are divisible by 5
# for loop
divisible_numbers = {}
for num in range(1, 101):
    if num % 5 == 0:
        divisible_numbers[num] = num**3
print(divisible_numbers)

# same exercise as above but with while loop
dict3 = {}
num = 1
while num < 101:
    if num % 5 == 0:
        dict3[num] = num**3
    num +=1
print(dict3)

dict4 = {1:"Donald", 2:"Mickey",3:"Bugs",4:"Daffy", "five":"Spongebob"}
print(dict4)
print(type(dict4))
print(dict4.keys())
print(dict4.values())
for k in dict4.keys():
    print(k)
    print(dict4[k])

for k in dict4.keys():
    if dict4[k] == "Bugs":
        print("Value Bugs has key:", k)

# use the value method to iterate through each value in the dictionary
print(dict4.values())
for val in dict4.values():
    print(val)

#outputs the key:value pairs as tuples
print(list(dict4.items()))
dict5 = {"elina":123, "john":"hall",45:376, "gate":345.76}

#find the number of times each word occurs in the string:
str1 = "Journyx technology, from the source code of our software to the code that maintains our Web site and ASP sites, is entirely based on Python. It increases our speed of development and keeps us several steps ahead of competitors while remaining easy to read and use. It's as high level of a language as you can have without running into functionality problems. I estimate that Python makes our coders 10 times more productive than Java programmers, and 100 times more than C programmers."
words = str1.split()
word_count = {}
for word in words:
    if word not in word_count.keys():
        word_count[word] = words.count(word)
print(word_count)

# counts how many times the letter appears in the string
str1 = "Journyx technology, from the source code of our software to the code that maintains our Web site and ASP sites, is entirely based on Python. It increases our speed of development and keeps us several steps ahead of competitors while remaining easy to read and use. It's as high level of a language as you can have without running into functionality problems. I estimate that Python makes our coders 10 times more productive than Java programmers, and 100 times more than C programmers."
letter_count = {}
for char in str1:
    if char in letter_count.keys():
        letter_count[char]+=1
    else:
        letter_count[char] = 1
print(letter_count)


for key in sorted(letter_count.keys()):
    if letter_count[key] >1:
        print(key, letter_count[key])

# find unique elements in dictionary
# same results as code above
str1 = "Journyx technology, from the source code of our software to the code that maintains our Web site and ASP sites, is entirely based on Python. It increases our speed of development and keeps us several steps ahead of competitors while remaining easy to read and use. It's as high level of a language as you can have without running into functionality problems. I estimate that Python makes our coders 10 times more productive than Java programmers, and 100 times more than C programmers."
list1 = str1.split()
dict = {}
for i in list1:
    dict[i] = list1.count(i)
print(dict)
