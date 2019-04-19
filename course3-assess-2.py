#Assessment: Advanced Accumulation

#Qn1
lst_check = ['plums', 'watermelon', 'kiwi', 'strawberries', 'blueberries', 'peaches', 'apples', 'mangos', 'papaya']

map_testing = map((lambda value: "Fruit: " + value),lst_check)

#Qn2

countries = ['Canada', 'Mexico', 'Brazil', 'Chile', 'Denmark', 'Botswana', 'Spain', 'Britain', 'Portugal', 'Russia', 'Thailand', 'Bangladesh', 'Nigeria', 'Argentina', 'Belarus', 'Laos', 'Australia', 'Panama', 'Egypt', 'Morocco', 'Switzerland', 'Belgium']
b_countries = filter(lambda item: 'B' in item, countries)
print(b_countries)

#Qn3
people = [('Snow', 'Jon'), ('Lannister', 'Cersei'), ('Stark', 'Arya'), ('Stark', 'Robb'), ('Lannister', 'Jamie'), ('Targaryen', 'Daenerys'), ('Stark', 'Sansa'), ('Tyrell', 'Margaery'), ('Stark', 'Eddard'), ('Lannister', 'Tyrion'), ('Baratheon', 'Joffrey'), ('Bolton', 'Ramsey'), ('Baelish', 'Peter')]
first_names = [name[1] for name in people]

#Qn4
lst = [["hi", "bye"], "hello", "goodbye", [9, 2], 4]
lst2 = [2*x for x in lst]

#Qn5
students = [('Tommy', 95), ('Linda', 63), ('Carl', 70), ('Bob', 100), ('Raymond', 50), ('Sue', 75)]
passed = [x[0] for x in students if x[1]>=70]

#Qn6
l1 = ['left', 'up', 'front']
l2 = ['right', 'down', 'back']
x = zip(l1,l2)
opposites = filter(lambda i: len(i[0])>3 and len(i[1])>3 ,x)
print(opposites)

#Qn7
species = ['golden retriever', 'white tailed deer', 'black rhino', 'brown squirrel', 'field mouse', 'orangutan', 'sumatran elephant', 'rainbow trout', 'black bear', 'blue whale', 'water moccasin', 'giant panda', 'green turtle', 'blue jay', 'japanese beetle']

population = [10000, 90000, 1000, 2000000, 500000, 500, 1200, 8000, 12000, 2300, 7500, 100, 1800, 9500, 125000]
pop_info = list(zip(species, population))
print(pop_info)

endangered = [i[0] for i in pop_info if i[1]<2500]
print(endangered)
