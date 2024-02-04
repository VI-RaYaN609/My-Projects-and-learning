class vehicle:
    doors = 4
    wheels = 4
    engine = 1                      
    def __init__(self,brand,model,year,color):      #this each self will have its own variable       
        self.brand = brand
        self.model = model
        self.year = year
        self.color = color

    def drive(self):
        print("{} is driving!!".format(self.brand,self.model))
    def stop(self):
        print("{} {} is stopped".format(self.brand,self.model))
class flying:
    def fly():
        print("Flying")

class car(vehicle):
    pass                                  # all self will have the same variable 'doors','wheels'......
class motorcycle(vehicle):
  doors = 0
  wheels = 2
class helicopter(vehicle,flying):
    pass
class planes(vehicle,flying):
    pass
