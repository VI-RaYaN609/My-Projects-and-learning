# lambda function = function written in 1 line using lambda keyword accepts any number of argumetns,
#                   but only has one expression.
#                   (think of it as a shortcut)
#                   (useful if needed for a short period of time ,throw-away)

#lambda parametres:expression

#def square(x):
#    return x*x

square = lambda x:x*x

print(square(4))