"""
4 Pillars of OOP
1. Encapsulation
2. Abstraction
3. Inheritance
4. Polymorphism

1. Class - blueprint of an object
2. Object - instance of class
3. Attributes - characteristics
4. Methods - Functions(Actions)
"""
class Car:
    #Constructor Method - Entrance of the class
    def __init__(self, color, year, model):
        #Encapsulation or data hiding
        self.__color = color
        self.__year = year
        self.__model = model

    #Getters and setters
    def setColor(self, color):
        self.__color = color

    def getColor(self):
        return self.__color

#Creating an object of a class
car1 = Car("Yellow", 2010, "BMW")
print(car1.getColor())
car1.setColor("Blue")
print(car1.getColor())