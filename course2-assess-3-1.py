#Assessment: Functions

#Qn1
def int_return(x):
    return x
    
#Qn2
def add(x):
    return x + 2

#Qn3
def change(x):
    words = "Nice to meet you!"
    newstring = x + words
    return newstring
    
#Qn4
def accum(x):
    tot = 0
    for i in x:
        tot = tot + i
    return tot

#Qn5
def length(x):
    c = 0
    y = "Less than 5"
    for i in x:
        c = c + 1
    if c > 4:
        y = "Longer than 5"
    return y

#Qn6
def divide(x):
    z = x / 2 
    return z

def sum(x):
    z = divide(x) + 6
    return z


