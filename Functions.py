# add two numbers
def add(num1: int, num2: int) -> int:
    num3 = num1 + num2

    return num3

# Driver code
num1, num2 = 5, 15
ans = add(num1, num2)
print(f"The addition of {num1} and {num2} results {ans}.")

# check if number is prime
def is_prime(n):
    if n in [2, 3]:
        return True
    if (n == 1) or (n % 2 == 0):
        return False
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    return True
print(is_prime(78), is_prime(79))

# check if number is even or odd
def evenOdd(x):
    if (x % 2 == 0):
        print("even")
    else:
        print("odd")
evenOdd(2)
evenOdd(3)

# use * in function if number of kids is unknown
def my_function(*kids):
  print("The youngest child is " + kids[2])
my_function("Emil", "Tobias", "Linus")

def my_function(food):
  for x in food:
    print(x)

fruits = ["apple", "banana", "cherry"]

my_function(fruits)


import math
square_root = math.sqrt(4)
print("Square root of 4 is", square_root)
power = pow(2,3)
print("2 to the power 3 is", power)

# Ex 1:
# you want to know how long it will take to deliver each one of the packages assuming you always ride your bike at 20 miles per hour
# time = distance / speed
# print time taken for each one of the places
# bethesda distance = 3.4 miles
# georgetown distance = 2.6 miles

def time_taken(dist,speed):
    '''This function calculates time taken given distance and speed'''
    timeTaken = round(dist/speed)
    return timeTaken  # you are returning the value that is being calculated

# main program
location_1 = 'Bethesda'
distance_1 = 3.4
speed_1= int(input("speed for Bethesda is:"))
time1 = time_taken(distance_1,speed_1) # calling the function
print("The time for Bethesda is:",time1)

location_2 = 'Bloomingdale'
distance_2 = 100
speed_2 =20
time2 = time_taken(distance_2,speed_2)
print("The time for Bloomingdale is:",time2)

location_3 = 'Georgetown'
distance_3 = 2.6
speed_3 = 10
time3 = time_taken("The time for Georgetown is:",distance_3,speed_3)

total_time = time1 + time2 + time3
print(f'The total time is: {total_time}')

#Ex2: create a function to add three numbers
def add_numbers(num1,num2,num3):
    print("Initial numbers:",num1,",",num2,",",num3)
    sum = num1 + num2 + num3
    return sum
# main program begins in the first position
sum = 0
sum = add_numbers(4,5,6) # call function
print("Sum is:",sum)

#Ex3
# Create a function that finds the sum of squares of 5 numbers
def squares(num1,num2,num3,num4,num5):
    return num1 ** 2 + num2 ** 2 + num3 ** 2 + num4 ** 2 + num5 ** 2
sum_of_squares = squares(1,2,3,4,5)
print("Sum of squares is:",sum_of_squares )

# now change the function so that it squares the even numbers and cubes the odd numbers and then returns the sum of these squares and cubes
def add_numbers(num1, num2, num3):
    print (num1, num2, num3)
    list1 = [num1, num2, num3]
    sqr = 0
    cub = 0
    total = 0
    for i in list1:
        if i%2==0:
            sqr = i**2
            total = total + sqr
        elif i%3 == 0:
            cub = i**3
            total = total + cub
        else:
            total = total+i

    return (total)

#main program
x = 10
y = 13
z = 21

sum = 0
sum = add_numbers(x, y, z) #calling the function
print (sum)

sum = add_numbers(2, 5, 3)
print (sum)




