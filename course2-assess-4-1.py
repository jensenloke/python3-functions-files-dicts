#Assessment: More about Iteration

#Qn1
def sublist(x):
    n = 0
    list = []
    while(n<len(x)):
        if x[n] == 5:
            break
        list.append(x[n])
        n = n + 1
    return list
    
#Qn2
def check_nums(x):
    n = 0 
    list = []
    while(n<len(x)):
        if x[n] == 7:
            break
        list.append(x[n])
        n = n + 1
    return list

#Qn3
def sublist(x):
    n = 0
    list = []
    while(n<len(x)):
        if x[n] == "STOP":
            break
        list.append(x[n])
        n = n + 1
    return list

#Qn4
def stop_at_z(x):
    n = 0
    list = []
    while(n<len(x)):
        if x[n] == "z":
            break
        list.append(x[n])
        n = n + 1
    return list


#Qn5
sum1 = 0

lst = [65, 78, 21, 33]

for x in lst:
    sum1 = sum1 + x

sum2 = 0
n = 0 
while(n<len(lst)):
    sum2 = sum2 + lst[n]
    n = n + 1

if sum2 == sum1:
    print("True")
    
#Qn6
def beginning(x):
    n = 0
    list = []
    while(n<len(x)):
        if x[n] == "bye":
            break
        list.append(x[n])
        n = n + 1
    return list[:10]

