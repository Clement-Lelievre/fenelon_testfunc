a = 3
b = 5
a=4
#print(a*b-b)
city  = "P a r i s"
#print(3*len(city))
# 3*len(city)

# len([1,2,5,6,9])
def fenelon_longueur(toto):
    o = 0
    for letter in toto:
        o = o + 1
    print(o)

#print(fenelon_longueur('Ba+---^???!rcelone'))
#print(fenelon_longueur('r')* 5 )
#print(type(78.9), type('pi'))

# def check_arobas(email):
#     if type(email) != str:
#         print('Email incorrect1')
#     elif '@' in email:
#         print('OK')
#     else:
#         print('Email incorrect2')
        
# check_arobas(3.14)

# def ma_fonction(arg1, arg2):
#     return arg1 + arg2

# print(ma_fonction(3,5))

city = "pARIS"
city = 'paris'
city='pariSs'
#print(lower(city))
#print(city.lower().capitalize())

#print(city.endswith("s"))


# print le nom de chaque élève dont le prénom a une longueur < 4

# students = ['max','julie','mbape','zidane', 'lea']
# for person in students:
#     if len(person) < 4 :
#         print(person)
        
# print le nom en majuscule de chaque élève dont la dernière lettre est 'a'

# students = ['max','julie','tata','mbape','zidane', 'lea']
# for person in students:
#     if person.endswith('a'):
#         print(person.upper())
  
l = [1,2.5,'toto',3.14,[5,6]]
# print les éléments n'étant pas de type float

# for f in l:
#     if type(f)!= float:
#         print(f)

city = 'Paris'*2
while len(city)>4:
    print(city)
    city = city[:-1]