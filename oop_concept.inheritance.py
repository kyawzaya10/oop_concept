class Vechicle():
    def printVechicle(self):
        print("Hello from Vehicle!")

class Factory():
    def printFactory(self):
        print("Hello from Factory!")

class Car(Vechicle, Factory):
    #Method overriding
    def printVechicle(self):
        super().printVechicle()
        print("Hello from Car!")
    #Method adding
    def printHello(self):
        print("Hello from another Car!")

car1 = Car()
car1.printVechicle()
car1.printHello()
car1.printFactory()
