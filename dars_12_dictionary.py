# dict = {'name':'Islom', 'surname':'Jorayev', 'color': 'red', 'height': 1.90, 'width': 5.20}
# # print(dict)


# favourite = {'Ahmad':'bugatti', 'Asil':'ferrari', 'Akrom':'BMW', 'Ismoil':'porsche', 'Akmal':'lambo'}
# # print(f'{favourite["Ahmad"]} {favourite["Akmal"]} {favourite["Akrom"]}')


# workdays = {'float':'onlik sonlar', 'integer':'sonlar', 'if':'agar', 'else':"yo'qsa", 
#             'string':'matinlar', 'list':'list', 'tuple':'tuple', 'set':'set',}
# # print(workdays)
# print(workdays['float'])
# workdays['operators'] = 'operatorlar'
# print(workdays)

# a = workdays.get('sonlar'.lower(), 'error')
# print(a)
# print(workdays.get('float'.lower(), 'none'))
# del workdays['string']
# print(workdays)


# cars = {'ferrari': 1950, 'bugatti': 'shiron', 'lamborgini':'latest version', 'supra':'mtx',
#         'LE9':'mozilla'}
# for k, q in cars.items():
#     a = input('what car would you like to order? ')
#     if a == k or q:
#         print('when are you buying')
#     else:
#         a != k or q
#         print('this car is not on sale!')


# cars = {
#     "supra": 1_500_000,
#     'bugatti': 2_000_000,
#     'bmw': 150_000,
#     'ferrari': 300_000
# }
# # car = ['supra', 'ferrari']
# car = input('car')
# for i in cars:
#     if i in car:
#         print(f'{i}-${cars[i]}')
#     else:
#         i not in car
#         print('car is not on sale')

# car = {
#     'model': 'supra',
#     'price': "1_900_000",
#     'made in': 'china',
# }
# a = input('enter key: ')
# for i in car.items():
#     if a in i:
#         print(f'{i}')
#     else:
#         a not in i 
#         print("this information is not found")


# a = input("enter key: ")
# b = car.get(f"{a}", 'error')
# print(b)

# numbers = [1,4,2,3,5]
# print(sorted(numbers, reverse=True))

# a = int(input('enter number'))
# print(a+1)


# dict = {
#     'Akmal': '97-727-72-93',
#     'Usmon': '99-323-94-23',
#     'Ahmad': '90-943-12-80'
# }
# print(f"{dict['Ahmad']}. "
#       f"{dict['Akmal']}. ")
# dict.clear()
# print(dict)

# for i in dict:
#     if i in 'Akmal':
#         print(i.values())
#     elif i in 'Usmon':
#         print(i.values())
#     else:
#         i in 'Ahmad'
        
        
# family = {
#     'adxam':'super boy',
#     'akmal':'my brother',
#     'aziz':'my borther',
#     'muslima':'my little sister'
# }
# for i,v in family.items():
#     # print(f'{i} who is {v}')
#     if f'{i}' in 'adxam':
#         print('hello brother')
#     else:
#         print('error')
        
# names = {
#     'Akrom':'ferrari',
#     'Laziz':'porsche',
#     'rustam':'bugatti',
#     'hakim':'bmw',
#     'asil':'mercedez'
# }
# print(f'{names["Akrom"]} '
#       f'{names["hakim"]} '
#       f'{names["Laziz"]}')


# car1 = {
#     'made': 'mercedes',
#     'model': 'gelik',
#     'color': 'qora',
#     'year': 2024,
#     'price': 50_000
# }
# car2 = {
#     'made': 'bmw',
#     'model': 'x7',
#     'color': 'qora',
#     'year': 2024,
#     'price': 45_000
# }
# car3 = {
#     'made': 'hummer',
#     'model': 'h2',
#     'color': 'qora',
#     'year': 2024,
#     'price': 85_000
# }
# # car = {car1, car2, car3}
# a = input('enter the car\'s name: ')
# b = car1.get(f'{a}', 'error')
# print(b)

# ----------------------------------------------------
# dars 3
# classwork no_1

# RolseRoyce = []
# for i in range(20):
#     newCar = {
#         'made': "Rolse Royce",
#         'model': "Phantom",
#         'color': None,
#         'year': 2024,
#         'price': None,
#         'engine': None,
#         'km': None,
#     }
#     RolseRoyce.append(newCar)
# # print(RolseRoyce)

# for i in RolseRoyce[:10]:
#     i['color'] = 'brown'
#     i['engine'] = 'automatic'

# for i in RolseRoyce[10:20]:
#     i['color'] = 'white'
#     i['engine'] = 'mechanic'

# for i in RolseRoyce:
#     if i['engine'] == 'automatic':
#         i['price'] = 85_000
#         i['km'] = 10_000
#     elif i['engine'] == 'mechanic':
#         i['price'] = 70_000
#         i['km'] = 20_000
#     else:
#         i['price'] = 50_000
#         i['color'] = 'green'
    

# for i in RolseRoyce:
#     print(i.values())

# ---------------------------------------------------------------

# no_2
# names = []
# for i in range(10):
#     friend = {
#         'name':'Adxam',
#         'surname':'Axatov',
#         'yold': None,
#         'born_year': None,
#         'location': None,
#         'school': None
#     }
#     names.append(friend)
#     # print(names)
# for i in names[:5]:
#     i['born_year'] = 2006
#     i['location'] = 'olmazor'

# for i in names[5:8]:
#     i['location'] = 'qibray'
#     i['born_year'] = 2007

# for i in names[8:10]:
#     i['location'] = 'yunusobod'
#     i['born_year'] = 2008

# for i in names:
#     if i['born_year'] == 2006:
#        i['yold'] = (2024-2006)
#     elif i['born_year'] == 2007:
#        i['yold'] = (2024-2007)
#     else:
#         i['born_year'] == 2008
#         i['yold'] = (2024-2008)

# for i in names:
#     if i['location'] == 'olmazor':
#         i['school'] = '32-maktab'
#     elif i['location'] == 'qibray':
#         i['school'] = '16-maktab'
#     else:
#         i['location'] == 'yunusobod'
#         i['school'] = '235-maktab'

# for i in names:
#     print(i.values())

# ------------------------------------------------------

# no3
# names = {
#     'Ahamd':{
#         'behaviour':'excelent',
#         'good':'friend',
#         'the look':'elegant',        
#         'manner':['good', 'nice', 'lovely', 'extroverted', 'good-looking', 'awsome']

#     },
#     'Asilbek':{
#         'manner':'satisfactory',
#         'age':17,
#         'school': '32-school' ,       
#         'manner':['good', 'nice', 'lovely', 'extroverted', 'good-looking', 'awsome']

#     },
#     'Ismoil':{
#         'good':'guy',
#         'age': 18,
#         'manner':['good', 'nice', 'lovely', 'extroverted', 'good-looking', 'awsome']
#     }
# }

# for i,k in names.items():
#     # print(k.values())
#     print(f'my man {i} is a good man with a good features like {k.values()}')
#     for a in k['manner']:
#         print(a, end=' ')

# ------------------------------------------------------------

# names = {
#     'adxam':{
#         'familiya':'axatov',
#         'yoshi':18,
#         'tugilgan yili': 2006,
#         'tel nomer': [97_795_72_93, 99_727_72_93],
#         'chet tillari': ['rus tili', 'ingliz tili', 'ozbek tili']
#     },
#     'akmal':{
#         'familiya':'axatov',
#         'yoshi':17,
#         'tugilgan yili': 2007,
#         'tel nomer': [97_843_27_93, 99_947_56_39],
#         'chet tillari': ['nemis tili', 'ingliz tili', 'ozbek tili', 'rus tili']
#     },
#     'ahmad':{
#         'familiya':'abduvahobov',
#         'yoshi':18,
#         'tugilgan yili': 2006,
#         'tel nomer': [90_846_12_48, 99_944_55_82],
#         'chet tillari': ['rus tili', 'ispan tili', 'ozbek tili']
#     },
#     'ismoil':{
#         'familiya':'abduvahobxojaev',
#         'yoshi':16,
#         'tugilgan yili': 2008,
#         'tel nomer': [94_100_10_40, 99_124_43_51],
#         'chet tillari': ['rus tili', 'ozbek tili']
#     }
# }
# for info,values in names.items():
    # print(f'\n{info.upper()}')
    # # for i in values.values():
    # #     print(i)
    # for i in values['chet tillari']:
    #     print(*i.title())
    # for i in values['tel nomer']:
    #     print(i)


# --------------------------------------------------------------


# countries = {
#     'argentina':{
#         'wealth':'10 billion $',
#         'area': '2,700,000 sqkm',
#         'energy': '44,000,000 kv',
#         'population': '46,948,000 people',
#         'languages': ['spanish', 'english', 'italian', 'french', 'german']
#     },
#     'uzbekistan':{
#         'wealth':'25 billion $',
#         'area': '787,000 sqkm',
#         'energy': '88,452,000 kv',
#         'population': '38,948,000 people',
#         'languages': ['qazaq', 'english', 'turk', 'russian', 'japanese']
#     },
#     'america':{
#         'wealth':'10 billion $',
#         'area': '4,233,030 sqkm',
#         'energy': '150,000,000 kv',
#         'population': '400,948,000 people',
#         'languages': ['spanish', 'english', 'italian', 'french', 'german', 'portugese', 'latin']
#     }
# }
# for i,l in countries.items():
#     # print(f'\nIn {i.title()} people speak these following languages:')
#     print(f'\nHere is {i.title()}\'s all stats:')
#     for a in l.values():
#     # for a in l.items():
#         print(a)
    # for b in l['languages']:
    #         print(b)

a = []
for i in range(1):
    countries = {
        'argentina':{
            'wealth':'10 billion $',
            'area': '2,700,000 sqkm',
            'capital':None,
            'energy': None,
            'population': None,
            'languages': ['spanish', 'english', 'italian', 'french', 'german']
        },
        'uzbekistan':{
            'wealth':'25 billion $',
            'area': '787,000 sqkm',
            'capital':None,
            'energy': None,
            'population': None,
            'languages': ['qazaq', 'english', 'turk', 'russian', 'japanese']
        },
        'america':{
            'wealth':'10 billion $',
            'area': '4,233,030 sqkm',
            'capital': None,
            'energy': None,
            'population': None,
            'languages': ['spanish', 'english', 'italian', 'french', 'german', 'portugese', 'latin']
        }
    }
a.append(countries)
# print(a)

# for i in countries











