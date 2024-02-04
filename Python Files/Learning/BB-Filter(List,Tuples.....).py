# filter() = creates a collection of elements from an iterable for which a function returns

#filter(function , iterable)

Users = [("User 1",20),
         ("User 2",14),
         ("User 3",15),
         ("User 4",40),
         ("User 4",38)]
age = lambda age:age[1]>=18

Adult_users = list(filter(age,Users))

for i in Adult_users:
    print(i)