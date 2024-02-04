#map() = applies a function to each item in an iterable (list,tuple .....)
#map(function,iterable)

store = [("water",1.00),
         ("Orange Juice",2.50),
         ("Lemon Juice",2.50),
         ("Coffe",4.00)]

bruh = {"bruh":1,
        "ok":2}

convert_euro  = lambda data:(data[0],data[1]*0.82)
convert_dollars=  lambda data:(data[0],data[1]/0.82)
convert_dollars_dict= lambda key,value:(key,value/0.82)

store_euros = list(map(convert_euro,store))
store_dollars = list(map(convert_dollars,store))

bruh_dollars = list(map(convert_dollars_dict,bruh.keys(),bruh.values()))
for i in bruh_dollars:
    print(i)

for i in store_euros:
    print(i)