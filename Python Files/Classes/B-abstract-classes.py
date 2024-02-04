#Prevents a user from creating an onbject of that class 
# + compels a user to override abstarct methods in a child class

#abstract class = a class which contains one or more abstract methods.
#abstract method = a method that has a declaration but does not have an implementation

from abc import ABC,abstractmethod  #you need to import these to use them

class animal(ABC) :                            
    @abstractmethod
    def sleep(self):                          # after doing these two steps you will not be able to create a something from 
        print("animal is sleeping")           # the class animal 

    def eating(self):
        print("animal is eating")
        
class flyer(animal) :
    def sleep(self):
        print("Flying animal is sleeping")

class land(animal) :
    def eating():
        print("Dog is eating")

bird = flyer()

bird.sleep()                          #can create bird because the class 'flyer' does have the abstractmethod 'sleep'
bird.eating()                          
                          
dog = land()                          #cant create dog because the class 'dog' doesn't have abstractmethod 'sleep'

dog.sleep()
dog.eating()

anim = animal()

anim.eating
anim.sleep