class phone:
    def __init__(self, company, model, color):
        self.company = company
        self.model = model
        self.color = color

    def setColor(self, color):
        self.color = color
    def getColor(self):
        return self.color


phone1 = phone("nothing", 1, "white")

phone1.setColor("black")
print(phone1.getColor())

class Company():
    def printCompany(self):
        print("Apple")

class Factory():
    def printFactory(self):
        print("FoxxCom")

class Phone(Company, Factory):
    def printCompany(self):
        print("Hello")

    def printFactory(self):
        print("Bello")
phone1 = Phone()

phone1.printCompany()
phone1.printFactory()

