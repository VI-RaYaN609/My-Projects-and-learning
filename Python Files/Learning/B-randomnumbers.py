import random   
import secrets   #for security generating purpuses 
a = random.randint(1,10)   #generate random number between 1 and 10
b = random.random()        #generate random number between 0 and 1 

list = [1,2,3,4,5]
List = [1,2,3,4,5]
c = random.choice(list)    #choose one of list items randomly
d = random.choices(list)  
random.shuffle(List)   #shuffle List
print(a,b,c)
print (d)
print(List)



                       #secrets
z = secrets.randbelow(100)            #generate a number below 100
y = secrets.choice(list)              #pick randomly one item from 'list'
random_hex = secrets.token_hex(16)
random_url = secrets.token_urlsafe(16)
print(y)
print(z)
print(random_hex)
print(random_url)
