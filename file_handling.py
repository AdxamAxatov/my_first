# with open('hello_world', 'w') as h:
#     h.write('hello world\n')
#     h.write('my name is anton')


# import pickle

# info1 = {
#     'name': 'anton',
#     'age': 25,
#     'city': 'baku'
# }
# info2 = {
#     'name': 'elena',
#     'age': 28,
#     'city': 'london'
# }

# with open('info.pkl', 'wb') as f:
#     pickle.dump(info1, f)
#     pickle.dump(info2, f)

# with open('info.pkl', 'rb') as f:
#     new1 = pickle.load(f)
#     new2 = pickle.load(f)

# print(new1)
# print(new2)


# user = input('Enter your username: '), input('Enter your password: ')  

# with open('users.txt', 'a') as f:
#     f.write(f'{user[0]}\n{user[1]}\n')



menu = {
    "lavash":{
        "mini lavash": 25_000,
        "big lavash": 32_000,
        'pishloqli lavash': 35_000,
        'tovuqli lavash': 28_000,
    },
    "pizza":{
        'danar pizza': 45_000,
        'oddiy pizza': 35_000,
        'qazili pizza': 45_000,
        'peporoni pizza': 35_000,
        },
    "gamburger":{
        'oddiy gamburger': 25_000,
        'cheese burger': 25_000,
        },
    "ichimliklar":{
        'cola': 20_000,
        'fanta': 18_000,
        'flavis': 18_000,
        'sprite': 18_000,
        'pepsi': 18_000,
        },}

for i in menu:
    print(f"\n{i.upper()}:")  
    for k,v in menu[i].items():
        print(f"{k.upper()}: {v}")  

# while True:
#     user = input('choose the food you would like to order: ')
#     for i in menu:
#         for k,v in menu[i].items():
#             if user in k or v:
                
             






















