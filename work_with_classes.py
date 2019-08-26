# Here, I'm going to try and explain (and understand) classes.
# Classes are templates that can store attributes, just like int or str. Str is a type of class that you can do things
# to, like .upper() or + 6.

# Methods are similar to functions. Their key difference is that they only work to run and do things with the class it's part of
#



# Inheritance

# Here, I'm creating a more general class. This class can have other classes as children, and those children can
# inherit attributes and methods such as (fillUpTank) or self.price

class Vehicle:
    def __init__(self, price, gas, color):
        self.price = price
        self.gas = gas
        self.color = color

    def fillUpTank(self):
        self.gas = 100

    def emptyTank(self):
        self.gas = 0

    def gasLeft(self):
        return self.gas


vehicle1 = Vehicle("$100", 100, "black")

class Car(Vehicle): # This turns the car into a child class of Vehicle
    def __init__(self, price, gas, color, speed):
        super().__init__(price, gas, color) # Super allows us to inherit the __init__ method
        self.speed = speed

    def beep(self):
        print("Beep Beep!")


class Truck(Vehicle): # This turns the car into a child class of Vehicle
    def __init__(self, price, gas, color, tyres):
        super().__init__(price, gas, color) # Super allows us to inherit the __init__ method
        self.tyres = tyres

    def beep(self):
        print("Honk Honk!")

jimtruck = Truck("$100", 60, "red", 8)
jimtruck.emptyTank()
print(jimtruck.gasLeft())
print("Chicken")

# Overloading methods
# When you type 5 + 7, Python automatically understands what your doing. It knows how to add those two numbers together.
# If you have two strings, such as "Chickpea" and "462345", the best way to "add" them is to append one to the other.
# Someone had to write methods to do this. Overloading methods basically means making our own methods to do things with.

# Here, I'm trying to add "coordinates" together. In other words, I want to be able to go p1 + p2 and so on
# without having to reference their attributes outside the class.


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
        self.coords = (self.x, self.y)

    def move(self, x, y):
        self.x += x
        self.y += y

    def __add__(self, p):
        return Point(self.x + p.x, self.y + p.y)

    def __sub__(self, p):
        return Point(self.x - p.x, self.y - p.y)

    def __mul__(self, p):
        return self.x * p.x + self.y * p.y

    def length(self):
        import math
        return math.sqrt(self.x**2 + self.y**2)

    def __gt__(self, p):
        return self.length() > p.length()

    def __ge__(self, p):
        return self.length() >= p.length()

    def __lt__(self, p):
        return self.length() < p.length()

    def __le__(self, p):
        return self.length() <= p.length()

    def __eq__(self, p):
        return self.x == p.x and self.y == p.y

    def __str__(self):
        return "(" + str(self.x) + "," + str(self.y) + ")"

p1 = Point(3,4)
p2 = Point(3,2)
p3 = Point(1,3)
p4 = Point(0,1)

p8 = (p4 - p3)
print(p8)
print(p1 == p2)
print(p1 > p2)
print(p4 <= p3)



# Static and Class methods
# Static and class methods are complicated. The basic rundown is this:
# Static methods do not reference the class nor an object/instance, and so doesn't do anything with the class. You
# Reference them by going [Class].[Method]

# The point of Static Methods is when you want to use them as a function but you want to organise them in a class
# A possible use for it is if I want to make my own personal math module, for example, to import into other programs.
class Math:
    @staticmethod
    def add(x, y):
        return x + y

# Note: Put @classmethod or @staticmethod before the methods to tell the program what they are

# Class methods are methods that can be run by the class itself, without the need for an instance of the class to be running.
# As long as you can call something that isn't dependent on each instance, you can also go [Class].[Method]

# Class methods are useful if you want to access class variables without having to pass in an object, because it's just
# going to pass in the class name that you've given it.

class Dog:
    dogs = []

    def __init__(self, name):
        self.name = name
        self.dogs.append(self)

    @classmethod
    def num_dogs(cls):
        return len(cls.dogs)

    @staticmethod
    def bark(n):
        # Barks n times
        for i in range(n):
            print("Bark!")

Dog.bark(5)
Jim = Dog("Jim")
print(Jim.num_dogs())
# @staticmethod and @classmethod are known as decorators. These serve to tell the program that these aren't regular methods
# because otherwise the computer will get mad because you didn't pass in "self". It also serves as a visual representation.

# Side note: Class variables are variables that are used in the class itself and can be called without the need of an
# instance of that class to be running.




# Private and Public Classes (and how to import your own classes into other files)

# Technically, Python doesn't really have a "private or public" class. We can imitate one with pseudo private classes,
# but there isn't really a way to implement it.

# Public Class
# A public class can be accessed by everyone. This means that any class can use this public classes fields/methods.
# Furthermore, other classes can modify public fields unless the field is declared as final.

# Private Class
# A private class can only be used within a certain file or within a certain scope. The way you make a class private
# is by adding a single underscore before the class name. This can also work for methods.

# In fact, the only reason we ut an underscore is to show to other programmers (and ourselves) that this class/method is private.
# In other words, it's a note that you shouldn't use the class for anything public because you don't want other classes
# be able to use it and mess with the class.

class _Private: # This class is "private".
    def __init__(self, name): #This means that all the methods in it are "private" as well
        self.name = name

class notPrivate: # This class is not private.
    def __init__(self, name): # All of it's classes are available for use.
        self.name = name
        self.priv = _Private(name)

    def _display(self): # However, this method specifically is marked as private.
        print("Hello")

    def display(self):
        print("Hi")


# It is possible to import modules into your code. However, it is also possible to use your code as a module for other code.


import work_with_classes  # If I were to use this in another file (and this were in the same directory
notPrivate = work_with_classes.notPrivate  # I would have access to all the functions and classes from that file