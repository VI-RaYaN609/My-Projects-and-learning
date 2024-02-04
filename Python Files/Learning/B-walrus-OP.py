# walrus operator  :=

#assignment expression aka walrus operator 
#assigns values to variables as part of a larger expression EXAMPLE ::

#foods = list()
#while True :
#    food = input("What food do you like ?:")
#    if food =="quit":
#        break
#    foods.append(food)

# Same program but shorter :

foods = list()
while food := input("What food do you like?:")!="quit":
    foods.append(food)

#you cant write this 'print(food=foods)' but you can write this :
print(food:=foods)