import random

class player :
    alive = True
    score = 100
    max_health = 100
    health = 100
    armor = 0
    damage = 15
    stamina = 100
    speed = 15
    upgrade_armor_price= 50
    upgrade_health_price= 50
    upgrade_damage_price= 50
    upgrade_speed_price= 50
    upgrade_stamina_price = 50

    def upgrade_armor(self):
        something = self.armor +10
        self.armor=something
        price = self.upgrade_armor_price*2
        self.upgrade_armor_price=price

    def upgrade_health(self):
        something = self.max_health +self.max_health*0.5
        self.max_health=something
        price = self.upgrade_health_price*2
        self.upgrade_health_price=price

    def upgrade_damage(self):
        something = self.damage + self.damage*0.5
        self.damage = something
        price = self.upgrade_damage_price*2
        self.upgrade_damage_price=price

    def upgrade_speed(self):
        something = self.speed +self.speed*0.5
        self.speed=something
        price = self.upgrade_speed_price*2
        self.upgrade_speed_price=price

    def upgrade_stamina(self):
        something = self.stamina +self.stamina*0.5
        self.stamina=something
        price = self.upgrade_stamina_price*2
        self.upgrade_stamina_price=price

class organism :
    pass
class animal(organism):
    alive = True
    def flea(self):
        print("animal is running!!")
    def attack(self):
        print("animal is attacking")
    def ivestegate(self):
        print("Animal is investegating")
    def sleep(self):
        armor = self.armor + self.armor*0.5
        self.armor = armor

class plants(organism):
    pass
class dog (animal):
    name = "dog"
    health=75
    armor = 0
    damage = 25
    speed = 25
    prize =random.randint(40,55)
    def alpha(self):
        damage =self.damage+self.damage*0.25
        self.damage = damage
        armor = self.armor + 20
        self.armor = armor
        self.prize += self.prize*0.2
        self.name="Alpha dog"
    def pack(self,pack_number):
        armor =self.armor-self.armor*0.05*pack_number
        self.armor = armor
    
class cat (animal):
    name = "cat"
    health = 25
    armor = 0
    damage = 5
    speed = 25
    prize = random.randint(10,20)
    
class bear (animal):
    name = "bear"
    health = 400
    armor = 0
    damage = 45
    speed = 20
    prize = random.randint(112,150)

class snake (animal):
    name = "snake"
    health = 40
    armor = 0
    damage = 15
    speed = 5
    prize = random.randint(15,30)

class deer (animal):
    name = "deer"
    health = 100
    armor = 0
    damage = 40
    speed = 60
    prize = random.randint(45,60)

