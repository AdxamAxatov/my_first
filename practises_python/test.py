# transports = {
#     'avtobus':{
#         'speed limit': 60,
#         'price': 1700,
#         'person limit': 24,
#         'car price': 50_000_000,
#         'comfortability': 'more space'
#     },
#     'taxi':{
#         'speed limit': 80,
#         'price': 15_000,
#         'person limit': 5,
#         'car price': 150_000_000,
#         'comfortability': 'fast service'
#     },
#     'damas': {
#         'speed limit': 70,
#         'price': 5_000,
#         'person limit': 7,
#         'car price': 70_000_000,
#         'comfortability': 'available every time'
#     },
#     'ferrari': {
#         'speed limit': 150,
#         'price': 100_000,
#         'person limit': 1,
#         'car price': 200_000_000,
#         'comfortability': 'super speed'
#     },
#     'limuzin': {
#         'speed limit': 50,
#         'price': 150_000,
#         'person limit': 10,
#         'car price': 100_000_000 ,
#         'comfortability': 'luxurious'
#     },
#     'marshrut': {
#         'speed limit': 40,
#         'price': 2_000,
#         'person limit': 15,
#         'car price': 30_000_000,
#         'comfortability': 'cheap'
#     },
#     'matiz': {
#         'speed limit': 70,
#         'price': 10_000,
#         'person limit': 4,
#         'car price': 30_000_000,
#         'comfortability': 'cheap'
#     },
#     'cobalt': {
#         'speed limit': 80,
#         'price': 20_000,
#         'person limit': 5,
#         'car price': 100_000_000,
#         'comfortability': 'good-looking'
#     },
#     'yukmashina':{
#         'speed limit': 30,
#         'price': 50_000,
#         'person limit': 1,
#         'car price': 60_000_000,
#         'comfortability': 'none'
#     },
#     'kamaz': {
#         'speed limit': 50,
#         'price': 30_000,
#         'person limit': 1,
#         'car price': 45_000_000,
#         'comfortability': 'none'
#     }
# }
# for i in transports:
#     print(f"\n{i}")
#     for k,v in transports[i].items():
#         print(f'{k.lower()}: {v}')    
# number = 0
# option = ''
# user = ''
# new = ''
# while True:
#     user = input('\nchoose the options: ')
#     if user in transports:
#         for k,v in transports[user].items():
#             print(f'{number+1} {k.upper()}:{v}')
#             number += 1
#             if k == 'yukmashina':
#                 print('this truck cannot take people! ')
#     else:
#         user not in transports
#         print('you can only choose the option given above! ')
    

        # if 'person limit' in transports:
        #     new = 'person limit'
        # if new < 2:
        #     percap = 'person limit'
    # option = int(input('how many people are needed: '))
    # if option <= percap:
    #     print('we cannot take this less people')
    
    
    # if transports[user]:
    # elif user not in transports:
    #     print('you need to enter the options mentioned above!')
    #     # user += input('\nchoose the option: ')
    # if option <= 2:
    #     print('we cannot take less than 3 people! ')
    #     # user += input('\nchoose the option: ')
    # if user == transports['yukmashina']:
    #     print('sorry, we cannot take the order! ')

      

# lst = []
# my = ['ona', 'ota', [15, 56, 'matn', [25, 'opa', 'uka'], ['aka']], 2, 5, 8, 'akam']
# for i in my:
#     if type(i) == list:
#         for j in i:
#             if type(j) == list:
#                 for k in j:
#                     if type(k) == list:
#                         for l in k:
#                             lst.append(i)
#                     else:
#                         lst.append(k)
#             else:
#                 lst.append(j)
#     else:
#         lst.append(i)

# print(lst)  
    
    
    
   
    




            


        













































