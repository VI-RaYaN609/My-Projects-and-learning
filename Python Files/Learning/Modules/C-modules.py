#module = a file containing code .may contain functions,classes,etc....
#used with modular programming which is to seperate a program into parts

#to show all modules in python use 
#help("modules")

import module1           
#import module1 as msg                  #this will name module1 as msg
#from module1 import division,message   #this will import only division and message
#from module1 import*                   # this will import all 

x=module1.division(5,0)
print(x)
name = input("Enter your name :")
y=module1.message(name)