fruits = ['apple', 'orange', 'banana', 'kiwi', 'mango']
print(fruits[2])

# backwards index starts at -1, forward index starts at 0
numbers = [23, 45, 12, 67, 89, 100, 2, 5, -5]
print(numbers[0]*numbers[7])

# extracts elements at index 3 (which is 67) up to, but not including, index 5 (which is 89)
print(numbers[3:5])

# extract a sub-list starting at index 3 (67) and goes all the way to the end of the list
print(numbers[3:])

# slicing with just a colon : refers to the entire list
print(numbers[:])

# accesses the last element of the list
print(numbers[-1])

#  extracts a sub-list from the beginning of the list, but not including, the last element (which is -5)
print(numbers[:-1])
print(numbers[-3:-1])
print(numbers[::-1]) # reverse order

# prints the first five elements of the list, starting from index 0 (23) up to, but not including, index 5 (89)
print(numbers[:5])

# prints the whole list even though it doesn't have 99 elements
print(numbers[0:99])

# number of elements in the list
print(len(numbers))

del(numbers[3])
print(numbers)

squares = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121]
var2 = 5
if var2 in squares:
    print ("5 is in the list")

if var2 not in squares:
    print ("var2 not in squares")

even_num = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
even_num.append(22)
print(even_num)
even_num.insert(even_num.index(22), 21)
print(even_num)
even_num[::-1]
print("list reversed:",even_num)
len(even_num)
print("The length of the list is", len(even_num))
del even_num[4]
print(even_num)
print("The new length of the list is", len(even_num))
num = [6,7,21]
if num in even_num:
    print(f"{num} is in the list")
if num not in even_num:
    print(f"{num} is not in the list")

list1 = [1,3,5,7,9,11]
list1.append("Elina")
print("After append the new list is:",list1)
print(type(list1))
print(list1.remove("Elina"))
del(list1[0])
list1.insert(2,231)
print("After insert the new list is:",list1)
print(max(list1))

# string is immutable collection
str1 = "This is American University. It is a great place to study"
print(str1[3:9])
# seperates by space if empty, splits by ., etc
list2 = str1.split(".")
list2 = str1.split("a")
print(list2)
print(list2[1])
str2 = " ".join(list2)
print(str2)
str3 = ";".join(list2)
print(str3)

# matrix

# range function
num = [0,1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]
sum1 = 0
for i in num:
    sum1 = sum1 + i
print(sum1)

sum1 = 0
for i in range(302):
    sum1 = sum1 + i
print(sum1)

# use the range to find the product of first 15 numbers
product = 1
for i in range(1,5):
    product = product * i
print(product)

# use the range function find the product of multiples of 4 between 0 and 527
for i in range(4, 528, 4):
    product *= i
    print(product)

# multiples of 5 from 0 to hundrend
for i in range(0,100,5):
    numsqr = i**2
    numsqrplus = numsqr + 4
    print(numsqrplus)


# print buzz for all multiples of 5 and 7 from 3 to 302 (both number included)
for i in range(3,303):
    if i % 4 == 0 and i % 7 == 0:
        print(i,"Buzz")