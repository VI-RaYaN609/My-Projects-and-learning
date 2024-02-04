def message(name):
    print("Hello {},I'm Ben .Have a great day".format(name))
def division(num1,num2):
    try:
        result=num1/num2
        return result
    except Exception as error:
        return error
        