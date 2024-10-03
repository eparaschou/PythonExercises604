def my_function(a, b=10, c=20):
    return a + b + c

for i in range(5):
    if i == 3:
        print(i)
    continue


# Write a function find_pattern that takes in a list of integers and returns True if it contains 007 in order.
def find_pattern(nums):
    pattern = [0, 0, 7]
    count = 0
    for i in nums:
        if i == pattern[count]:
            count += 1
            if count == len(pattern):
                return True

    return False

print(find_pattern([1, 2, 4, 0, 0, 7, 5]))
print(find_pattern([1, 7, 2, 0, 4, 5, 0]))

import matplotlib.pyplot as plt
university = ['AU', 'GMU', 'ISU', 'VTU']
num_students = [138, 205, 232, 78]
plt.figure(figsize=(8, 5))
plt.plot(university, num_students, marker='o', linestyle='-', color='b', linewidth=2, markersize=8)
plt.title('Number of Students in Different Universities')
plt.xlabel('University')
plt.ylabel('Number of Students')
plt.tight_layout()  # Ensures labels are not cut off
plt.show()


class Player:
    def __init__(self, name, age, height, weight, total_score):
        self.name = name
        self.age = age
        self.height = height
        self.weight = weight
        self.total_score = total_score

    def isStarPlayer(self):
        if self.total_score * 3 >= 100:
            return "Star player"
        else:
            return "Not a star player"


player1 = Player("Elina", 24, 165, 55, 58)
player2 = Player("Sam", 18, 160, 55, 25)

print(player1.isStarPlayer())
print(player2.isStarPlayer())


def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False

print(is_leap_year(2024))
print(is_leap_year(2019))




class Shape:
    def __init__(self, length, width):
        self._length = length
        self._width = width

    def get_length(self):
        return self._length

    def set_length(self, length):
        self._length = length


    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width


    def __str__(self):
        return f"Shape with length={self._length} and width={self._width}"


    def area(self):
        return self._length * self._width


    def paintingCost(self, price_per_sqft):
        return self.area() * price_per_sqft

if __name__ == "__main__":
    shape1 = Shape(5, 4)
    print(shape1)
    print(f"Area: {shape1.area()} square units")
    print(f"Painting cost at $2 per sqft: ${shape1.paintingCost(2)}")

    shape1.set_length(7)
    shape1.set_width(3)
    print(shape1)
    print(f"Area after update: {shape1.area()} square units")

import pandas as pd
df = pd.read_csv('December_Sleep_data_Sheet_dirty.csv')
df_cleaned = df.dropna()
df_cleaned = df_cleaned.drop_duplicates()
print("\nCleaned DataFrame:")
print(df_cleaned.head())





