from organism import *
from time import sleep
from random import randint


running = True
cycles =0
predatore = None
yes=["yes","ye","y"]
lookaround = ["look","lookaround","go","search"]
health_upgrade =["health","health u","health up","health upg","health upgrade"]
armor_upgrade =["armor","armor u","armor up","armor upg","armor upgrade"]
damage_upgrade =["damage","damag","damage u","damage up","damage upg","damage upgrade"]
user_input = ["look","go","search","heal","quit","lookaround","health","health u","health up","health upg","health upgrade","armor","armor u","armor up","armor upg","armor upgrade","damage","damag","damage u","damage up","damage upg","damage upgrade"]
user_inpute = ["look","go","search","heal","quit","lookaround","health upgrade","armor upgrade","damage upgrade"]

def Predator_picker():
    j=randint(0,25)
    if j >= 20:
        predator = bear()
    elif j>=10:         
        i=randint(0,50)
        predator = dog()
        if i>35:
           predator.alpha()
    else :
        predator = snake()
    return predator

def Player_attack (player1,predator):
    i=randint(0,100)
    if i>25:
        darmor = predator.armor/100
        predator.health -=player1.damage-player1.damage*darmor
        if predator.health<=0:
             predator.health=0
        print("You attacked the {0}! .{0}'s Health :{1}".format(predator.name,predator.health))
        sleep(3)
    return predator.health

def Predator_attack (player1,predator):
    i = randint(0,100)
    if i>=50:
        darmor = player1.armor/100
        player1.health -=predator.damage-predator.damage*darmor
        if player1.health <=0:
            player1.health =0
        print("{} Bit you!.Your Health:{}".format(predator.name,player1.health))
        sleep(3)
    return player1.health

def Berries_Eat(player1):
    #Eating Bad Berries
    if randint(1,51)>=30:
        debuff =randint(int(player1.max_health*0.15),int(player1.max_health*0.35))
        player1.health -=debuff
        print("Aghhhh!")
        sleep(1)
        print("Those berries made your tongue numb")
        sleep(0.5)
        print("Health lost:{}".format(debuff))
        if player1.health<=0:
            player1.alive =False
            player1.health =0
            print("You are dead")

        return player1.health
             #Eating Good Berries  
    else :
        buff = randint(int(player1.max_health*0.15),int(player1.max_health*0.35))
        player1.health +=buff
        print("Yummy...")
        sleep(1)
        print("Those berries gave you a boost in your health")
        sleep(0.5)
        print("Health added:{}".format(buff))  
        
        return player1.health
  
