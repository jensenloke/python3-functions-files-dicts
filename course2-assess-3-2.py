#Assessment: Tuples

#Qn1
olympics = ("Beijing", "London", "Rio", "Tokyo")

#Qn2
tuples_lst = [('Beijing', 'China', 2008), ('London', 'England', 2012), ('Rio', 'Brazil', 2016, 'Current'), ('Tokyo', 'Japan', 2020, 'Future')]
country = []
for i in tuples_lst:
    country.append(i[1])
print(country)

#Qn3
olymp = ('Rio', 'Brazil', 2016)
city, country, year = olymp

#Qn4
def info(name, gender, age, bday_month, hometown):
    return name, gender, age, bday_month, hometown

#Qn5
gold = {'USA':31, 'Great Britain':19, 'China':19, 'Germany':13, 'Russia':12, 'Japan':10, 'France':8, 'Italy':8}
num_medals = []
for k,v in gold.items():
    num_medals.append(v)

print(num_medals)

