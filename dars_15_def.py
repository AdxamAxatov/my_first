# user = int(input('>>>> '))
# if user % 2 == 0:
#     print(user)
# else:
#     user % 2 != 0
#     user += 1
#     print(user)


# def juflovchi(raqam):
#    print(raqam +(raqam % 2))
    
# juflovchi(int(input('>>> ')))


# def fio(fullname, age):
#     print(f'{fullname} {2024 - age} years old')

# fio(input('enter your full name: ').title(), int(input('enter your born year: ')))




# def karra(raqam):
#     print(f'{raqam} sonnning kvadrati {raqam**2}')
#     print(f'{raqam} sonning kubi {raqam**3}')

# karra(int(input('>>> ')))


# def definer(number):
#     if number % 2 == 0:
#         print('it is even number')
#     else:
#         number % 2 == 1 
#         print('it is odd number')
    
# definer(int(input('>>> ')))


# user = int(input('enter 1st number '))
# user2 = int(input('enter 2nd number '))
# if user > user2:
#     print(f'{user} is greater than {user2}')
# else:
#     user < user2
#     print(f'{user2} is greater than {user}')


# def user(st : int, nd : int):
#     if st > nd:
#         print(f'{st} is greater than {nd}')
#     else:
#         st < nd
#         print(f'{nd} is greater than {st}')

# user(int(input('enter 1st number: ')), int(input('enter 2nd number: ')))
 
 
# def num(a, b, c):
#     if a > b:
#         if a > c:
#             print(a, b, c)
#         else:
#             print(c, a, b)
#     if b > c:
#         if b > a:
#             print(b, c, a)
#         else:
#             print(a, c, b)
#     if a > c:
#         if a > b:
#             print(c, b, a)
#         else:
#             print(b, a, c)
    
    
# num(int(input('enter 1st number: ')), int(input('enter 2nd number: ')), int(input('enter 3rd number: ')))



# def num(a, b, c):
#     if a >= b and a >= c:
#         if b >= c:
#             print(a, b, c)
#         else:
#             print(a, c, b)
#     elif b >= a and b >= c:
#         if a >= c:
#             print(b, a, c)
#         else:
#             print(c, b, a)
#     else:
#         print(c, b, a)

# num(int(input('enter 1st number: ')), int(input('enter 2nd number: ')), int(input('enter 3rd number: ')))


# def user_info(fullname, age, birthplace, phonenumber, email):

#     info = {
#         'fullname': fullname,
#         'age': age,
#         'birthplace': birthplace,
#         'phonenumber': phonenumber,
#         'email': email
#     }
#     return info

# user = user_info(input('enter your full name: ').title(), int(input('enter your age: ')),input('enter your adress: '), int(input('enter your phone number: ')), input('enter your email: '))
# for k,v in user.items():
#     print(f'{k.capitalize()}: {v}')
    # for i in user:
    #     if i[fullname]:
    #         info['fullname'] = i[user]
    #     if i[age]:
    #         info['age'] = i[user]
    #     if i[birthplace]:
    #         info['birthplace'] = i[user]
    #     if i[phonenumber]:
    #         info['phonenumber'] = i[user]
    #     if i[email]:
    #         info['email'] = i[user]


# def user(a, b, c):
#     if a > b and a > c:
#         return a
#     elif b > a and b > c:
#         return b
#     else:
#         return c
    
# new = user(int(input('enter 1st numbers: ')), int(input('enter 2nd numbers: ')), int(input('enter 3rd numbers: ')))
# print(f'{new} is the highest number among three numbers')



# def enter_price(price):
#     dct = {}
#     while price:
#         new = price.pop()
#         user = input(f'enter the price of {new}: ')
#         dct[new] = user
#     return dct

# price = ['laptop', 'phone', 'tablet']
# eneter = enter_price(price[:])
# print(eneter)
# print(price)



# def user(*user):
#     return sum(user)

# new = user(int(input('>>> ')), int(input('>>> ')), int(input('>>> ')), int(input('>>> ')))
# print(new)


# def user(*user: str):
#     for i in user:
#         print(i.title())

# user(input('enter only text: '))



# def user(nomi, yer_maydoni, aholisi, military_rank):
#     info = {
#         'nomi': nomi,
#         'yer maydoni': yer_maydoni,
#         'aholisi': aholisi,
#        'military rank': military_rank
#     }
#     return info

# print('davlat haqida malumot kirgazamiz!')
# new = user(input('nomi: ').title(), int(input('yer maydoni: ')), int(input('aholisi: ')), int( input('military rank: ')))
# print(new)


# def student_info(name, surname, **info):
#     info['name'] = name
#     info['surname'] = surname
#     return info

# user = student_info(input('name: ').title(), input('surname: ').title())
# print(user)


# lst = []
# response = ''
# while True:
#     user = input('add your favourite things: ')
#     lst.append(user)
#     for i in lst:
#         print(i)
#     response = input('do you want to add more? (yes/no): ')
#     if response == 'no':
#         break









