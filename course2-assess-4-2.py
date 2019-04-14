#Assessment: Advanced Functions

#Qn1
def mult(x,y=6):
    return x*y

#Qn2
def greeting(name, greeting="Hello ", excl="!"):
    return greeting + name + excl

print(greeting("Bob"))
print(greeting(""))
print(greeting("Bob", excl="!!!"))

#Qn3
def sum(intx, intz=5):
    y = intz + intx
    return y

#Qn4
def test(x, y = True, dict1 = {2:3,4:5,6:8}):
    if y == True:
        for k,v in dict1.items():
            if k == x:
                return v
    elif y == False:
        return y
    
#Qn5
def checkingIfIn(a,direction=True,d={'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return True
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return False
    
#Qn6
def checkingIfIn(a, direction = True, d = {'apple': 2, 'pear': 1, 'fruit': 19, 'orange': 5, 'banana': 3, 'grapes': 2, 'watermelon': 7}):
    if direction == True:
        if a in d:
            return d[a]
        else:
            return False
    else:
        if a not in d:
            return True
        else:
            return d[a]

# Call the function so that it returns False and assign that function call to the variable c_false
c_false = checkingIfIn('carrots',True)
print(c_false)
# Call the fucntion so that it returns True and assign it to the variable c_true
c_true = checkingIfIn('carrots',False)
# Call the function so that the value of fruit is assigned to the variable fruit_ans
fruit_ans = checkingIfIn('fruit')
# Call the function using the first and third parameter so that the value 8 is assigned to the variable param_check
param_check = checkingIfIn('pear',True) + checkingIfIn('watermelon',True)
print(param_check)
