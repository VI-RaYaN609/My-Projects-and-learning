from Zcars import *
from Zorganism import *

car_1=car("Porshe","911",2023,"darkblue")
car_2=car("Ferrari","812 SuperFast",2022,"BlazeRed")
print(car_1.brand)
print(car_1.model)
print(car_1.year)
print(car_1.color)
print("wheels : {}".format(car_1.wheels))
print("doors : {}".format(car_1.doors))
car_1.drive()
car_1.stop()

bike_1 =motorcycle("Ducati","V4s",2021,"red")
print(bike_1.doors)


print("////////")
dog_1 = dog()
dog_1.angry().scared()          # this is possible becasue of the return self in end of the function inside of the class of dog
print(dog_1.damage)
print("///////////////////")
class PrintAllClassWithJustName():
    def __init__(self,par1,par2):
        self.par1=par1
        self.par2=par2
    # This function will make sure when print class by its name it will print 
    # the string you type down there 
    def __str__(self):    
        return f"par1={self.par1}| par2={self.par2}"    

Test1 = PrintAllClassWithJustName("Hello",25)
print(Test1)