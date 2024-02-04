# sort() method = used with lists
# sort() function = used with iterables (tuples....)

cars = [("ferrari","812 SuperFast",2022),
        ("Porshe","911 TurboS",2023),
        ("Audi","RS3",2021),
        ("BMW","M8",2022)]

brand = lambda brands:brands[0]
model = lambda models:models[1]
year = lambda years:years[2]

#sort list alphabetecly                  #sort(key= ,reverse=)
#cars.sort()

#reverse 
#cars.sort(reverse=True)

#sort by key
#cars.sort(key=brand)
cars.sort(key=model)
#cars.sort(key=year)

for i in cars:
    print(i)

print("")

vehicules=  (("Audi","RS3",2021),
             ("BMW","M8",2022),
             ("ferrari","812 SuperFast",2022),
             ("Porshe","911 TurboS",2023),)

sorted_vehicules= sorted(vehicules,key=year)

for i in sorted_vehicules:
    print(i)