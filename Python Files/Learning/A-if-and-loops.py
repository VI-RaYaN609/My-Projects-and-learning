                      # if statements
while True :
    try:
       age = int(input("How old are you?:"))
       break
    except ValueError:
        print("Please enter a valid number")   
if age >=100:
    print("how are you alive !!") 
elif age<0 :
    print("You are probably still in your dads balls......")   
elif age>=18:
    print("you are an adult!!")
else :
    print("you are a minor!!")

                                        #!LOOPS
                                        #FOR loops
import time
print("ENTERING FOR LOOPS")
print("THIS IS FOR LOOP")
for i in range( 20 ,10-1 ,-1 ):            #range (10,20,2) is 10 to 20 with a cout up of 2 (end point is not displayed)
      print(i)                             #range (20,10-1,-1) this loop will go from 20 to 10 
      time.sleep(0.1) 
    
                                        #WHILE loops

print("THIS IS WHILE LOOP")
name=""
i=0
while len(name)<4:
    if i>0:
        print(f"Username cant {len(name)} have caracteres")
    name=input("Enter your name:")
    i+=1

    
