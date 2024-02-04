def test(Num1,Num2,Num3) :
    Result = (Num1+Num2)*Num3
    return Result

while True :#userinput for x
 try :
   
   x=int(input("give me a number1:"))
   break
 
 except ValueError:
   
   print("Unvalid number !.Try again:")


while True :#userinput for y
  try:
   
    y=int(input("give me a number2:"))
    break
  
  except ValueError:
   
    print("Unvalid number!.Try again")

z=2
print("Result =",test(Num1=x,Num3=z,Num2=y))
          #this will assure that x is Num1 |y is Num2|z is Num3 so if you write them with wrong order it wont matter

# *args = parameter that will pack all arguments into a tuple

def hi(*names):
  print(names)

hi("args1","args2","args3")
# **kwargs = parameter that will pack all arguments into a dictionary

def HI(**bruh):
  print(bruh)

HI(first="kwargs1",secound="kwargs2",third="kwargs3")

#*            Memory address of a function and assigning functions to variables 

def Hello():
  print("you just called Hello function")

address_of_Hello = Hello             #if you want its memory address dont use ()

print(Hello)
print(address_of_Hello)

address_of_Hello()

say = print
say("hello world")