                   #this while loop will make sure that the code will run and wont be interrupted 
                   #you can remove if as you like
while True:
       try:                                                   #it will run the code inside of try and if it runs into a error
          num1 = int(input("Enter a number to divide :"))     #it ill go to except     
          break
       except ValueError as error:
          print(error)
          print("Unvalide number!!")
while True:                           
    try :
      while True:
       try:    
          num2 = int(input("Enter a number to divide by :"))
          break
       except ValueError as error:
          print(error)
          print("Unvalide number")
      result = num1/num2
      print(result)
      break
    except ZeroDivisionError as error:
      print(error)
      print("You cant divide by zero !")
    except Exception as error:
      print(error)
      print("Error")
