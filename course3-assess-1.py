course_3_assessment_1

#Qn1
nested = [['dog', 'cat', 'horse'], ['frog', 'turtle', 'snake', 'gecko'], ['hamster', 'gerbil', 'rat', 'ferret']]
output = nested[1][2]

#Qn2
lst = [['apple', 'orange', 'banana'], [5, 6, 7, 8, 9.9, 10], ['green', 'yellow', 'purple', 'red']]

#Test to see if 'yellow' is in the third list of lst. Save to variable ``yellow``
for list in lst:
    if 'yellow' in list:
        yellow = True
print(yellow)

#Test to see if 4 is in the second list of lst. Save to variable ``four``
four = False
if 4 in lst[1]:
    four = True
print(four)

#Test to see if 'orange' is in the first element of lst. Save to variable ``orange``
orange = None
if 'orange' in lst[0]:
    orange = True
else:
    orange = False
print(orange)

#Qn3
L = [[5, 8, 7], ['hello', 'hi', 'hola'], [6.6, 1.54, 3.99], ['small', 'large']]

# Test if 'hola' is in the list L. Save to variable name test1
for lst in L:
    if 'hola' in lst:
        test1 = True
    else:
        test1 = False
print(test1)

# Test if [5, 8, 7] is in the list L. Save to variable name test2
if [5, 8, 7] in L:
    test2 =  True
else:
    test2 = False
print(test2)

# Test if 6.6 is in the third element of list L. Save to variable name test3
if 6.6 in L[2]:
    test3 = True
else:
    test3 = False
print(test3)

#Qn4
nested = {'data': ['finding', 23, ['exercises', 'hangout', 34]], 'window': ['part', 'whole', [], 'sum', ['math', 'calculus', 'algebra', 'geometry', 'statistics',['physics', 'chemistry', 'biology']]]}

# Check to see if the string data is a key in nested, if it is, assign True to the variable data, otherwise assign False.
print("Qn1------")
data = None
for k in nested:
    print(data)
    if k == 'data':
        data = True
        break
    else:
        data = False
print("--final value--")
print(data) 

print("Qn2------")
# Check to see if the integer 24 is in the value of the key data, if it is then assign to the variable twentyfour the value of True, otherwise False.
twentyfour = False
for item in nested['data']:
    if item == 24:
        twentyfour = True

print(twentyfour)

print("Qn3------")
# Check to see that the string 'whole' is not in the value of the key window. If it's not, then assign to the variable whole the value of True, otherwise False.
for item in nested['window']:
    if item == 'whole':
        whole = False
print(whole)

print("Qn4------")
# Check to see if the string 'physics' is a key in the dictionary nested. If it is, assign to the variable physics, the value of True, otherwise False.
physics = False
for k in nested:
    print(k)
    if k == 'physics':
        physics = True
    print(physics)
    
#Qn5
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}
for k,v in nested_d['London'].items():
    if k == 'Great Britain':
        london_gold = v
        print(london_gold)

#Qn6
sports = {'swimming': ['butterfly', 'breaststroke', 'backstroke', 'freestyle'], 'diving': ['springboard', 'platform', 'synchronized'], 'track': ['sprint', 'distance', 'jumps', 'throws'], 'gymnastics': {'women':['vault', 'floor', 'uneven bars', 'balance beam'], 'men': ['vault', 'parallel bars', 'floor', 'rings']}}

# Assign the string 'backstroke' to the name v1
v1 = sports['swimming'][2]
# Assign the string 'platform' to the name v2
v2 = sports['diving'][1]
# Assign the list ['vault', 'floor', 'uneven bars', 'balance beam'] to the name v3
v3 = sports['gymnastics']['women']
# Assign the string 'rings' to the name v4
v4 = sports['gymnastics']['men'][-1]

#Qn7
nested_d = {'Beijing':{'China':51, 'USA':36, 'Russia':22, 'Great Britain':19}, 'London':{'USA':46, 'China':38, 'Great Britain':29, 'Russia':22}, 'Rio':{'USA':35, 'Great Britain':22, 'China':20, 'Germany':13}}

US_count = []

for c,v in nested_d.items():
        for country,count in v.items():
            if country == 'USA':
                US_count.append(count)
print(US_count)

#Qn8
l_of_l = [['purple', 'mauve', 'blue'], ['red', 'maroon', 'blood orange', 'crimson'], ['sea green', 'cornflower', 'lavender', 'indigo'], ['yellow', 'amarillo', 'mac n cheese', 'golden rod']]
third = []
for item in l_of_l:
    print(item)
    third.append(item[2])
print(third)
    
#Qn9
athletes = [['Phelps', 'Lochte', 'Schooling', 'Ledecky', 'Franklin'], ['Felix', 'Bolt', 'Gardner', 'Eaton'], ['Biles', 'Douglas', 'Hamm', 'Raisman', 'Mikulak', 'Dalton']]
t = []
other = []
for list in athletes:
    for names in list:
        if 't' in names:
            t.append(names)
        else:
            other.append(names)
print(t)
print(other)
