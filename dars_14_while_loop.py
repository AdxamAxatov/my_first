# request = ' (press q to quit)\n '
# request += 'enter your favourite film: '
# a = str('')
# while a != 'q':
#     a = input(request).lower()
#     if a != 'q':
#         print(f'your favourite film is {a}')
    

# age = 'enter your age: '
# a = ''
# while True:
#     a = int(input(age).lower())
#     if a <= 7 or a >= 65:
#         print(f'the ticket is free for {a} age')
#     elif a > 7 and a <= 18:
#         print(f'the ticket is 25 sums for {a} age')
#     else:
#         a > 18 and a < 65
#         print(f'the ticket is 65 sums {a} age')
#     a = input('enter stop to quit or to carry on, enter continue: ').lower()
#     if a == 'stop':
#         break
#     else:
#         a == 'continue'
#         continue
    
    

# overall = 0
# body = int(input('how many ticket do you want to buy? '))
# ages = {
#     "young": 25_000,
#     'middle': 65_000,
#     'old_kid': 0,
# }
# for i in range(body):
#     bodies = int(input(f'enter {i+1}-person\'s age: '))
#     if bodies <= 7 or bodies >= 65:
#         print(f'the ticket is free for {bodies} age')
#         overall += ages['old_kid']
#     elif bodies > 7 and bodies <= 18:
#         print(f'the ticket is 25 sums for {bodies} age')
#         overall += ages['young']
#     else:
#         bodies > 18 and bodies < 65
#         print(f'the ticket is 65 sums {bodies} age')
#         overall += ages['middle']
# print(f'Overall price is {overall} sum')

# -----------------------------------------------------------------

# num = 1
# products = []
# print('we will take your products!')
# while True:
#     request = f'\n{num}-enter your food products: '
#     user = input(request)
#     products.append(user)
#     new = input('do you want to add more? (yes/no)')
#     if new == 'yes':
#         for i in products:
#             print(i)
#         continue
#     else:
#         break
# print('everything is listed:')
# for i in products:
#     print(i)

# products = {
#     'fruits':{
#         'apple': 15_000,
#         'banana': 10_000,
#         'cherry': 8_000,
#         'lemon': 12_000,
#         'apricote': 18_000
#     },
#     'chocolates':{
#         'dark chocolate': 10_000,
#         'white chocolate': 19_000,
#         'big chocolate': 14_000
#     },
#     'drinks':{
#         'cola': 10_000,
#         'pepsi': 8_000,
#         'fanta': 15_000,
#         'flavis': 5_000
#     }    
# }
# lst = []
# num = 0
# yesno = ''
# for i in products:
#     print(i.upper())
# while True:
#     if yesno == 'no':
#         break
#     request = '\nchoose the options: '
#     user = input(request)
#     if user in products:
#         for k,v in products[user].items():
#             print(f'{k.upper()}: {v}')
#     else:
#         print('it is not available')
    
#     users = input('what do you like to order? ')
#     if users in products[user]:
#         num += products[user][users]
#         lst.append(users)
#     else:
#         print('it is not available')
#     yesno = input('do you want to add more? (yes/no)')
#     print(f"Buyurtmalar: {[i for i in lst]}".replace("[", '').replace("]", ""))
#     print(f"Hisob: {num} so'm.")
    

# -------------------------------------------------------------------

# lst = ['axror', 'azam', 'abror', 'usmon', 'islom']
# dct = {}
# alochi = []
# yaxshi = []
# while True:
#     baho = lst.pop(dct)
#     for i in lst:
#         user = input('qaysi oquvchini baholamoqchisiz? ')
#         if user in i:
#             continue
#         else:
#             print('this pupil is not on the list! ')
#         new = int(input('baholang: '))
#         if new < 4:
#          yaxshi.append(new)
#         if new > 4:
#             alochi.append(new)
#         (alochi, yaxshi) = i
#         dct[i] = new
#     print(dct)
    
    
    

            



        








































