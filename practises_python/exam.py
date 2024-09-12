

# num = 0
# lst = ['algebra', 'ona tili', 'adabiyot', 'tarix', 'musiqa']
# for i in lst:
#     user = int(input(f'{i}ning bahosini kirgizing: '))
#     num += user
#     a = num/(len(lst))
#     if user > 5:
#         print('faqat maktab bahosini kirgazing! ')
# if a <= 5 and a >= 4.5:
#     print('you are excelent')
# elif a < 4.5 and a <= 4:
#     print('you are good')
# elif a < 3:
#     print('you are bad')
# print(a)   

# -------------------------------------------------------------

# user = int(input('hozirgi yilni kirgazing: '))
# user2 = int(input('tugilgan yilingizni kirgazing: '))
# print(f'sizni yoshingiz {user-user2}')

# -------------------------------------------------------------
# juft = []
# toq = []
# user = int(input('hohlagan soningizni kirgazing: '))
# for i in range(user):
#     if i % 2 == 0:
#         toq.append(i)
#     else:
#         juft.append(i)
# print(juft)

# --------------------------------------------------------------
# digit = str()
# alpha = []
# user = input('enter anything you want: ')
# for i in user:
#     alpha.append(i)
# alpha.sort()
# for i in alpha:
#     digit += i
# print(digit)
    

# ----------------------------------------------------------------
# lst = []
# overall = 0
# user = int(input('ixtiyoriy sonlar kirgazing: '))
# for i in range(user):
#     lst.append(user)
#     overall += user
# print(overall)
# # print(sum(user)) 

# ------------------------------------------------------------

# no1

# user = input('enter your name and surname: '), input('enter your age: ')
# with open('new.file', 'w') as w:
#      w.write(f'{user[0]}\n{user[1]}\n')

# students = ['adxam', 'usmon', 'diyorbek', 'sardor', 'aliy']
# for i in students:
#     user = input(f'{i.title()}, enter your adress: '), input('enter your age: ')
#     with open('new.file', 'w') as w:
#         w.write(f'{user[0]}\n{user[1]}\n')
         
     
# no2

# users = int(input('enter any number: '))
# if users % 15 == 0:
#     print('FizzBuzz')
# elif users % 3 == 0:
#     print('Fizz')
# elif users % 5 == 0:
#     print('Buzz')
# else:
#     print('none')


# no3
# a = input('enter smth: ')
# b = a[::-1]
# if b == a:
#     print('Bu polindrom')
# else:
#     print('Bu polindrom emas')


# no4
user = input('enter longer number: ')
for i in user:
    if user[:-2] in i:
        print(i)
        user1 = user.replace(i, "*")
    print(user)




























