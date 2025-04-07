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

# for i in RolseRoyce[:3]:
#     i['color'] = 'brown'
#     i['engine'] = 'automatic'
#     i['km'] = 5_000

# for i in RolseRoyce[3:6]:
#     i['color'] = 'white'
#     i['engine'] = 'mechanic'

# for i in RolseRoyce:
#     if i['engine'] == 'automatic':
#         i['price'] = 85_000
#     elif i['engine'] == 'mechanic':
#         i['price'] = 70_000
#     else:
#         i['price'] = 50_000

# for i in RolseRoyce:
#     print(i.values())


# ---------------------------------------------------------

# developers = {
#     'zilola': ['python', 'java', 'C#', 'c++', 'html', 'css', 'javascript'],
#     'sherzod': ['python', 'html', 'css'],
#     'usmon': ['python'],
#     'diyorbek': ['python', 'react', 'c#', 'javascript'],
#     'adxam': ['java', 'golang']
# }

# for names, languages in developers.items():
#     print(f"\n{names.title()}: ", end="")
#     for i in languages:
#         if i == languages[-1]:
#             print(f"{i.upper()}.", end=" ")
#         else:
#             print(f"{i.upper()},", end=" ")



talabalar = {
    'zilola': {
        'familiya': 'sherzodova',
        'ismi': 'zilola',
        'tyil': 2006,
        'tillar': ['english', 'koreys', 'turk']
    },
    'usmon': {
        'familiya': 'diyorbekov',
        'ismi': 'usmon',
        'tyil': 2005,
        'tillar': ['arab', 'english', 'xitoy', 'fransuz', 'nemis']
    },
    'sherzod': {
        'familiya': 'adxamov',
        'ismi': 'sherzod',
        'tyil': 1995,
        'tillar': ['english', 'turk', 'koreys']
    }
    }
for name, info in talabalar.items():
    print(f"{name.title()}")
    for i in info['tillar']:
        print(i)











