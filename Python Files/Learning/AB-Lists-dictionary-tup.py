                                    #! 1D Lists
food = ["tomato","salad","onion","cucumber"]
food.append("fruits")     #will add "fruits" to the list at the end
food.insert(0,"sugar")    #will add "sugar" in the index of 0 (tomato)
food.remove("tomato")     #will remove "tomato" from the list 
food.sort()               #will sort the list alphabetecly
food.reverse()            #This will reverse the order of the list
#food.pop()               #this remove last element
#food.clear()             #This will remove all of list items 
print("cucumber appeard:",food.count("cucumber"),"times")    # a =food.count("salad") a will have the number of appearence of salad
print(f"The index of salad:{ food.index("salad")}")          # a= food.index("salad") a will have the index of salad
print(food)

for i in food:
    print(i)
                                   #! 2D Lists
print("2D LISTS :")
players = ["rayan","imad","aymen","oussama"]
score = [50,15,25,30]
deaths = [2,4,5,3]
game = [players,score,deaths]

print(game)
print("////////////////////")
for i in game:
    print(i)
print("////////////////////")
for i in game:
    for j in i:
        print(j,end=" ")
    print("")
                               #! Tuples
print("////////////////////")
tuples = ("food","drinks","desert",25)
a = tuples.count("drinks")      #this will give you the number of "drinks" in this case 1
b = tuples.index("food")        #this will give you the index of "food" in this case its 0

print("The number of drinks is :",a)
print("The index of food is :",b)

for i in tuples:
    print(i)
                               #! SETS
                               
                               #sets are unordered,unindexed and cannot have duplicates
                               #which make it faster than list when you searching for an element in the set
print("////////////////////")
Set = {"fork","spoon","knife","knife","knife"}
Set2 = {"plate","bowl","knife"}
Set.add("napkin")
#Set.remove("knife")            #this will remove all "knife"from the set
#Set.clear()                    #remove every element

Set.update(Set2)               #this will add set2 to set1
difference = Set.difference(Set2)
print("Difference between set1 and set2 :",difference)
for i in Set:
   print(i)
                                #! DICTIONARIES
              
            #key   #value
print("////////////////////")
capitals = {'USA':'Washington DC',
             'Algeria':'Algeirs',
             'Russia':'Moscow',
             'China':'Beijing'}
#capital = capitals['Algeria']  #this work aswell but if you type germany for example it will crash cause it is not in the dictionary
capital = capitals.get('germany')
print("capital =",capital) 
a=capitals.keys()                     #a has all the dic keys
b=capitals.values()                   #b has all the dic values 
c=capitals.items()                    #c has all the dic keys and values (everything)
capitals.pop('USA')                   #this will remove USA(remove the key and the value)
capitals.update({'germany':'Berlin'}) #this will add germany as a key and berlin as a value to dic
capitals.update({'Algeria':'Oran'})  #this will change the value of the key Algeria to oran

print("Dictionary :",capitals)
