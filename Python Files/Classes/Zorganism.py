import random
colors = ["white","black","Red","Orange","grey"]
class organism :
    alive = True
class animal(organism):
    def eating(self):
        print("The animal is eating")
    def roaming(self):
        print("The animal is roaming")
class plants(organism):
    def sleep(self):
       print("The plant is sleeping")
class dog(animal):
    In_pack= False
    alpha_state = False
    default_health = 100
    default_damage = 25
    default_damage_intake=1
    default_speed = 1
    Health= default_health
    damage = default_damage
    damage_intake = default_damage_intake
    speed = default_speed
    color = random.choice(colors)
    if In_pack == True:
        damage_intake -= default_damage_intake*0.25
    if random.randint(0,25)>=20:
        alpha_state = True
    
    def flee(self):
        self.speed += self.default_speed*0.5
        print("The dog is fleeing")
        return self
    
    def scared(self):
        self.damage -= self.default_damage*0.25
        self.speed += self.default_speed*0.25
        print("The dog is scared")
        return self
    
    def angry(self):
        self.damage += self.default_damage*0.25
        print("The dog is angry")
        return self
    
class bear(animal):
    default_health = 400
    default_speed = 0.75
    default_damage= 70
    default_damage_intake = 1
    health = default_health
    speed = default_speed
    damage = default_damage
    damage_intake = default_damage_intake
    color = random.choice(colors)
    def sleep(self):
        self.damage_intake += self.default_damage_intake*0.25
        print("The Bear is sleeping")
        return self