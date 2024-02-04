# Higher Order Function = A function that either :
# 1- accepts a function as an argument 
#           OR
# 2- return a function


# 1-
def Big(text):
    return text.upper()
def small(text):
    return text.lower()
def text(function):
    text = function(input("What text you like it to be displayed? : "))
    return text

print(text(Big))
print(text(small))

# 2-
def divisor(x):
    def dividend(y):
        return y/x
    return dividend

divide = divisor(2)       # x = 2
print(divide(6))          # y = 6