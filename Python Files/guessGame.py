import random

answer = random.randint(0,1000)
print(answer)
user = answer -1 
i=0

while user !=answer :
    while True:
        try:
           user =int(input("Guess :"))
           break
        except ValueError:
            print("Enter a valid number!!")
    B=user-answer
    if user==answer:
        print("Correct answer is {}".format(answer))
        break
    if user>answer:
        if B<=100:
           print("High!!")
        else :   
           print("Too High!!")
    else :
        if B>-100:
            print("Low!!")
        else:    
            print("Too Low!!")
    i+=1
print ("Your score is {}".format(i))