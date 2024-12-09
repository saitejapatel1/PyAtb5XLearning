#1.they cant return-->non return
#no return type and no parameter/arguements
from cgitb import reset


def cinema():
    print("director")

cinema()

#2. no return type and with parametrt/arguement
def cinema(name):
    print("title", name)
cinema("pushpa2")

#3 no return type and with default arguement(propositinal arguement)
def is_cinema_defaultarg(name="animal"):
    print("title",name.upper())

is_cinema_defaultarg()
#multiple arguements
def multiple_arg(name1="sai",name2="teja"):
    print("multiple args-->",name1,name2)
multiple_arg("virat","kohli")

#4.arguement+return type
def sumof2(a,b):
    return a+b
result=sumof2(3,4)
print(result)

def sumof2number_default(num1=3,num2=4):
    print("i will sum 2 numbers")
    return num1 + num2
results=sumof2number_default(num1=3,num2=4)
print(results)
results=sumof2number_default(num1=5,num2=2)
print(results)
