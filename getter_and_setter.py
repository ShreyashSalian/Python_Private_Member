class Automobile(object):
    def __init__(self,make,model,milege,price):
        self.__make = make
        self.__model = model
        self.__milege = milege
        self.__price = price

    def set_make(self,value):
        self.__make = value

    def get_make(self):
        return self.__make

    def set_model(self,value):
        self.__model = value

    def get_model(self):
        return self.__model

    def set_milege(self,value):
        self.__milege = value

    def get_milege(self):
        return self.__milege

    def set_price(self,value):
        self.__price = value

    def get_price(self):
        return self.__price

    def get_value(self):
        self.__make = input("Enter The manufacturer of car : ")
        self.__model = int(input("Enter The model of the car : "))
        self.__milege = int(input("Enter the milege of a car : "))
        self.__price = int(input("Enter The price : "))

class Car(Automobile):
    def __init__(self,make,model,milege,price,door):
        Automobile.__init__(self,make,model,milege,price)
        self.__door = door

    def set_door(self,value):
        self.__door = value

    def get_door(self):
        return self.__door

    def get_value(self):
        Automobile.get_value(self)
        self.__door = int(input("Enter The Number of Door : "))

v  = Car('BMW',2019,12500,50000,2)
#v = Car()
v.get_value()
print("Make of car : ",v.get_make())
print("Model of car : ",v.get_model())
print("Milege of car : ",v.get_milege())
print("Price of car : ",v.get_price())
print("Number of Door in a Car are :",v.get_door())






