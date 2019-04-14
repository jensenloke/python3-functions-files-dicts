#Assessment: Sorting

#Qn1
letters = "alwnfiwaksuezlaeiajsdl"
sorted_letters = sorted(letters,reverse=True)

#Qn2
animals = ['elephant', 'cat', 'moose', 'antelope', 'elk', 'rabbit', 'zebra', 'yak', 'salamander', 'deer', 'otter', 'minx', 'giraffe', 'goat', 'cow', 'tiger', 'bear']
animals_sorted = sorted(animals)

#Qn3
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
list = []
for k,v in medals.items():
    list.append(k)
alphabetical = sorted(list)

#Qn4
medals = {'Japan':41, 'Russia':56, 'South Korea':21, 'United States':121, 'Germany':42, 'China':70}
sorted_dictionary = sorted(medals.keys(), key=lambda k: medals[k],reverse=True)
top_three = sorted_dictionary[0:3]

#Qn5
groceries = {'apples': 5, 'pasta': 3, 'carrots': 12, 'orange juice': 2, 'bananas': 8, 'popcorn': 1, 'salsa': 3, 'cereal': 4, 'coffee': 5, 'granola bars': 15, 'onions': 7, 'rice': 1, 'peanut butter': 2, 'spinach': 9}
most_needed = sorted(groceries.keys(), key=lambda k: groceries[k],reverse=True)

#Qn6
def last_four(x):
    z = abs(x) % 10000
    return z

ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]

sorted_ids = sorted(ids, key= last_four)

#Qn7
ids = [17573005, 17572342, 17579000, 17570002, 17572345, 17579329]
sorted_id = sorted(ids,key=lambda x:x%10000)

#Qn8
ex_lst = ['hi', 'how are you', 'bye', 'apple', 'zebra', 'dance']
lambda_sort = sorted(ex_lst, key=lambda x: x[1])
