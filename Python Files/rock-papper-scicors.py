import random

dic={
 "rock":"papper",
 "papper":"scissors",
 "scissors":"rock"
}
game=["rock","papper","scissors"]
computer=random.choice(game)

while True : 
 user= input("Choose rock|paper|scissors :")
 user=user.lower()
 if user in ["rock","paper","scissors"]:
  break
print("your choice:",user)
print("computer choise :",computer)
if user==computer:
 print("Damn a draw!! you both choose {}".format(user))
elif user=="rock":
   if computer=="scissors":
     print("you win!!")
   if computer=="paper":
     print("you lose!!")
elif user=="paper":
   if computer=="scissors":
     print("you lose!!")
   if computer=="rock":
     print("you win!!")
elif user=="scissors":
   if computer=="rock":
     print("you lose!!")
   if computer=="paper":
     print("you win!!")
