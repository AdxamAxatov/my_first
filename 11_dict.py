# Dictionry - Lug'at

# mother - ona

# key: value - kalit: qiymat
# my = {}
# my = dict()

# my_dct = {'nomi': "H2", 'made': 'Hummer', 'rangi': 'qora', "yili": 2009}
# print(my_dct)

# print(my_dct['made'])

student = {'ismi': 'sherzod usmonov', 
           'yoshi': 28,
           'tyil': 1994}

print(f"{student['ismi'].title()}. "
      f"{student['yoshi']}-yoshda. "
      f"{student['tyil']}-yilda tug'ilgan.")


car = {
    'made':'Ferrari',
    'model':'LaFerrari',
    'color':'black',
    'year':2024,
    'color':'red',
}

# print(car)

car['engine'] = 'automatic'
car['price'] = 600_000
# print(car)

car['price'] = 500_000
# print(car)
# print(len(car))

del car['color']
# print(car)




# get()
# sweet = car.get('narx', "Bunday key mavjud emas")
# print(sweet)
# print(car.get('narx'))
# print(car.get('narx', "Mavjud emas"))