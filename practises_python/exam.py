

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
# user = input('enter longer number: ')
# for i in user:
#     if user[:-2] in i:
#         print(i)
#         user1 = user.replace(i, "*")
#     print(user)




# def get_fractions(fraction1, fraction2):
    

#     numerator1, denominator1 = map(int, fraction1.split('/'))
#     numerator2, denominator2 = map(int, fraction2.split('/'))
#     total_numerator = numerator1 + numerator2
#     total_denominator = denominator1 + denominator2

#     if denominator1 == denominator2 or numerator1 == numerator2:
#         if denominator2 == denominator1:
#             return f"{fraction1} + {fraction2} = {total_numerator}/{denominator1}"

#         else:
#             numerator1 == numerator2
#             return f"{fraction1} + {fraction2} = {numerator1}/{total_denominator}"
        
#     return f"{fraction1} + {fraction2} = {total_numerator}/{total_denominator}"

# # a_b = '3/7'
# # c_b = '4/3'
# # result = get_fractions(a_b, c_b)
# # print(result)  

# def replacer(s: str) -> str:
#     """
#     Add your code here
#     """
#     return s.replace('"', "'").replace("'", '"')

# # hi = replacer("nono'mb")
# # print(hi)


# def is_palindrome(string):
   
#     left = 0
#     right = len(string) - 1

#     while left < right:
#         if string[left] != string[right]:
#             return False
#         left += 1
#         right -= 1

#     return True

# # Example usage:
# word = "racecar"
# print(is_palindrome(word))  # Output: True

# word = "hello"
# print(is_palindrome(word))  # Output: False











