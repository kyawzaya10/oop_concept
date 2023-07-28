class Calculator():
    def add(self, num1, num2):
        return num1 + num2

    def sub(self, num1, num2):
        return num1 - num2


class MyCal(Calculator):
    def expo(self, num):
        return num ** 2


mycal = MyCal()
print(mycal.sub(4, 2))
print(mycal.expo(5))

class Ornix():
    def multiply (self, num1, num2):
        return num1 * num2
class myOrnix(Ornix):
    def devv(self, num1, num2):
        return num1 // num2
myornix = myOrnix()
print(myornix.multiply(3, 4))
print(myornix.devv(3,4))
