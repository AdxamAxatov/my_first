9# Dictionary_2.0
phones = {
    'Usmon': "iPhone 15",
    'Adxam': "iPhone 16",
    'Diyorbek': "iPhone 14"
}

# for kalit, qiymat in phones.items():
#     print(f"{kalit.title()}ning telefoni: {qiymat}")

# print(phones.keys())


# for i in phones.keys():
# for i in phones:
#     print(i)



# print(phones.values())
# for i in phones.values():
#     print(i)


# smartphone = {
#     'Samsung 49': 1_500,
#     'iPhone 15': 1_200,
#     "Redmi": 500,
#     'iPhone 15': 1_500,
#     'iPhone 14': 1_300,
# }
# telefonlar = ['Redmi', 'iPhone 15']
# for i in smartphone:
#     if i in telefonlar:
#         print(f"{i} --- ${smartphone[i]}")


# for i in sorted(phones.keys()):
# for i in sorted(phones.values()):
#     print(i.title())


# cellphones = {
#     'zilola': 'iphone',
#     'usmon': 'iphone',
#     'diyorbek': 'samsung',
#     'adxam': 'samsung',
#     'ulugbek': 'redmi',
#     'sherzod': 'iphone'
# }
# for i in cellphones.values():
#     print(i)

# for i in set(cellphones.values()):
#     print(i)


# copy() - birorta bo'sh dict.ga ma'lumot nusxalab beradi.
# del() - butkul o'chirib beradi.
# clear() - tozalab beradi
# popitem() - sug'urib oladi.


car1 = {
    'made': 'mercedes',
    'model': 'gelik',
    'color': 'qora',
    'year': 2024,
    'price': 50_000
}
car2 = {
    'made': 'bmw',
    'model': 'x7',
    'color': 'qora',
    'year': 2024,
    'price': 45_000
}
car3 = {
    'made': 'hummer',
    'model': 'h2',
    'color': 'qora',
    'year': 2024,
    'price': 85_000
}
# print(f"{car1['made'].title()} "
#       f"{car1['model'].title()}")

# print(f"{car2['made'].title()} "
#       f"{car2['model'].title()}")

# print(f"{car3['made'].title()} "
#       f"{car3['model'].title()}")

car = [car1, car2, car3]
# for i in car:
#     print(f"{i['made'].title()} "
#           f"{i['model'].title()}")

print(car[0])






