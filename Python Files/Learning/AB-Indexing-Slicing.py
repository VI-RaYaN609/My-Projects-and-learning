                     #Indexing

Fullname = "Nibou Rayan"
                #  start stop step
Firstname = Fullname[:5]
lastname = Fullname[6:]
Inversed_Fullname = Fullname[::-1]

print(Firstname," "+lastname," "+Inversed_Fullname)

                     #slicing
Website = "https://youtube.com"

                   #Start stop step
websiteSlice = slice(8  , -4  ,  )             #this is used when you need to use the same slice multipule time for short code

websitename = Website[websiteSlice]   

print("#1",Website[websiteSlice])
print("#2",websitename)
print("#3",Website[slice(8,-4)])