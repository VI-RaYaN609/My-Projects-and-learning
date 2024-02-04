from organism import *
from consta import *
from time import sleep
from random import randint


while running :
   print("To play Enter play , to quit enter quit")
   Userinput = input()
   if Userinput.lower()=="quit":
      running = False
   if Userinput.lower()=="play":
     print("Hello RaYaN This game is made By me")
     player1=player()
     while player1.alive:
      
      print("{}$".format(player1.score))
      print("Health upgrade: {}$|Armor upgrade: {}$|Damage upgrade: {}$ ".format(player1.upgrade_health_price,player1.upgrade_armor_price,player1.upgrade_damage_price))
      print("Health :   {}/{}   |Armor :    {}     |Damage :   {}".format(player1.health,player1.max_health,player1.armor,player1.damage))
      
      #Checking User input 
      Userinput=input().lower()
      while Userinput not in user_input:
        print("Enter : {}".format(user_inpute))
        Userinput=input().lower()
     
      # quiting
      if Userinput=="quit":
        if input("You sure you wanna quit to desktop?:").lower()in yes:
          running = False
          break
      
      #healing
      if Userinput=="heal":
       if input("Are you sure you want to heal?.'cost 10$':").lower()in yes:
        if player1.health<player1.max_health: 
         if player1.score>=10:
           player1.health=player1.max_health
           player1.score-=10
           print("Healed succesfully",end=" ")
         else:
           print("Don't have enough credit for action!")
        else :
          print("You are already Fully Healed!.")

      #upgrades
      if Userinput in health_upgrade:
       if input("Are you Sure ?:").lower() in yes:
        if player1.score >=player1.upgrade_health_price: 
         player1.score -=player1.upgrade_health_price
         player1.upgrade_health()
         player1.health=player1.max_health
         print("Health Upgraded succesfully ")
        else:
         print("You dont have enough money for action!!")
      elif Userinput in armor_upgrade:
       if input("Are you Sure ?:").lower() in yes:
        if player1.score >=player1.upgrade_armor_price:  
         player1.score -=player1.upgrade_armor_price
         player1.upgrade_armor()
         print("Armor upgraded succesfully")
 
        else:
         print("You dont have enough money for action!!") 
      elif Userinput in damage_upgrade:
       if input("Are you Sure ?:").lower() in yes: 
        if player1.score >=player1.upgrade_damage_price:  
         player1.score -=player1.upgrade_damage_price
         player1.upgrade_damage()
         print("Damage upgraded succesfully")

        else:
         print("You dont have enough money for action!!") 
      
      #game cycle
      if Userinput in lookaround:
       #RNG
       i=randint(0,100)
       #First route
       if i in range(25):
          coin =randint(15,30)
          player1.score+=coin
          print("Great!! you found {} coins in the floor while walking!!. you have {}$".format(coin,player1.score))

       #Second route   
       elif i in range(25,75):
         
         # Predator picker
         predator =Predator_picker()
         

         #The FIGHT  
         print("you are fighting a {}".format(predator.name));sleep(1)
         print("Your Health : {}\t {} Health :{}".format(player1.health,predator.name,predator.health))
         while predator.health >0:
           
           #check for alive state
           if player1.health<=0:
             player1.alive =False
             print("You are dead.")
             break
           
          
          #Player attack predator
           predator.health=Player_attack(player1,predator)
            
          # predator attack player
           if predator.health >0:
             player1.health = Predator_attack(player1,predator)
         
         #fight Loss
         if player1.health<=0:break
         
         #Fight Win
         if player1.alive==True:
          print("You won the fight against a {}!!......".format(predator.name))
          print("Oh you found {}$ inside the dead body".format(predator.prize))
          player1.score +=predator.prize  
       
       #Third route
       elif i in range(75,101):
        
         i = randint(0,50)
         
         # Route 1
         if i>=20:
           coin =randint(20,30)
           player1.score -=coin
           print("You Tripped one a rock and fell on a hole !!")
           print("You passed out for a period of time..")
           print("You lost {} $ ".format(coin))

         # Route 2
         else :
           coin = randint(10,20)
           print("You found some berries that looks tasty ..")
           
           #user input for player choice
           user=input("Wanna eat them?:").lower()
           while user not in ["yes","no"]:
             user = input("Yes|No")
           
           #Berry Eating
           if user =="yes":
             player1.health=Berries_Eat(player1)
      
         
      print("")   