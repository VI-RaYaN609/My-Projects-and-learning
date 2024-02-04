#str.format() = optional method that gives users more control when displaying output

name = "rayan"
age = 18

text = "hello {}.I'm {} years old !!"
print("hello {}.I'm {} years old !!".format(name,age))
print("hello {0}.I'm {1} years old !!".format(name,age))
print("hello {Name}.I'm {Age} years old !!".format(Name=name,Age=age))
print(text.format(name,age))
                            #padding                            
print("///////////////////////////////")
print("this is padding {0:10}".format(name))
print("this is padding {0:<10} align to the left".format(name))
print("this is padding {0:>10} align to the right".format(name))
print("this is padding {0:^10} align to the middle".format(name))

                             #number formating
print("///////////////////////////////")
pi = 3.14159
number =1000
print("PI is = {:.2f}".format(pi))
print("organised number is :{:,}".format(number))
print("pi in sientific notation is :{:E}".format(pi)) 
print("1000 is in binary : {:b}".format(number))      #you cant change format of float to binary/octal/hex....
print("1000 in octal is : {:o}".format(number))      
print("1000 in hexadecimal is :{:X} ".format(number)) #X for uppercase x for lowercase