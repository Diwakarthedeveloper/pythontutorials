class Vehicle:
    def general_usage(self): # genral_usage is a method
        print("general use: transport")

class Car(Vehicle):
    def __init__(self) :
        print("I am Car")
        self.wheels = 4
        self.has_roof = True

    def specific_usage(self):
        self.general_usage()
        print("specific use: commute to work, vacation with family")

class MotorCycle(Vehicle):
    def __init__(self) :
        print("I am bike")
        self.wheels = 2
        self.has_roof = False

    def specific_usage(self):
        self.general_usage()
        print("specific use: road trip , racing")

c = Car()
#c.general_usage()  # genral usage is acalled above in he respected part
c.specific_usage()


m = MotorCycle()
#c.general_usage()
c.specific_usage()

print(isinstance(c, Car)) # show true means c is a object of car class
print(isinstance(c, MotorCycle)) # show false  means c is a not a object of car class

print(issubclass(Car,Vehicle)) # this will show true if car is a subclass of Vehicle
print(issubclass(Car,MotorCycle)) # this will show flase as car is not a subclass of Vehicle