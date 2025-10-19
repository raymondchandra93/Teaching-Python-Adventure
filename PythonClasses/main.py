import math

""" Phase 1 """


def distanceTo(x1, y1, x2, y2):
  dx = x1 - x2
  dy = y1 - y2
  distance = math.sqrt(dx**2 + dy**2)

  return distance


result = distanceTo(0, 0, 3, 4)
print(result)

""" Phase 2 """


# Class
class Point:

  # Constructor
  def __init__(self, x, y):
    self.x = x
    self.y = y

  # Method - what an object can do
  def calculateDistance(self, otherPoint):
    dx = self.x - otherPoint.x
    dy = self.y - otherPoint.y
    distance = math.sqrt(dx**2 + dy**2)

    return distance

  # Special Methods
  def __str__(self):
    return "Point X={}, Y={}".format(self.x, self.y)

  def __eq__(self, otherPoint):
    return self.x == otherPoint.x and self.y == otherPoint.y


# Object
p1 = Point(0, 0)
p2 = Point(3, 4)
p3 = Point(0, 0)

# Print the x and y of p1
print("p1.x = {}".format(p1.x))
print("p1.y = {}".format(p1.y))

print("p2.x = {}".format(p2.x))
print("p2.y = {}".format(p2.y))

# Call the method
dist = p1.calculateDistance(p2)
print(dist)

# Print an object
print(p1)
print(p1 == p3)

""" Phase 5 """

class Pet:
  # constructor
  def __init__(self, name, age):
    self.name = name
    self.age = age

  # method
  def walk(self):
    print("Pet is walking!")


class Cat(Pet):
  # Constructor
  def __init__(self, name, age):
    super().__init__(name, age)

  def meow(self):
    print("Meow")


class Dog(Pet):
  # Constructor
  def __init__(self, name, age):
    super().__init__(name, age)

  def walk(self):
    print("Go doggies go!")


C1 = Cat("Cattie", 1)
C1.meow()
print(C1.name, C1.age)

C2 = Dog("Doggie", 2)
C2.walk()
print(C2.name, C2.age)
