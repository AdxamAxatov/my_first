# age = input("Yoshingizni kiriting: ")
# age = int(age)
# print(f"Siz {2024-age}-yilda tavallud topgansiz!")



# age = input("Yoshingizni kiriting: ")
# try:
#     age = int(age) # Xato qaytargan qator
#     print(f"Siz {2024-age}-yilda tavallud topgansiz!")
# except:
#     print("Butun son kiritmadingiz")
# print("Dastur tugadi!")


# age = input("Yoshingizni kiriting: ")
# try:
#     age = int(age)
# except:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2024-age}-yilda tavallud topgansiz!")


# FAQAT MA'LUM BIR XATOLIKKA ISHLOVCHI FUNKISYALAR


# ValueError
# age = input("Yoshingizni kiriting: ")
# try:
#     age = int(age)
# except ValueError:
#     print("Butun son kiritmadingiz")
# else:
#     print(f"Siz {2024-age}-yilda tavallud topgansiz!")


# ZeroDivisionError
# a, b = 5, 10
# try:
#     b/(a-5)
# except ZeroDivisionError:
#     print("o ga bo'lib bo'lmaydi")


# IndexError
# fruit = ['banana', 'orange', 'apple', 'kiwi', 'lemon']
# try:
#     print(fruit[8])
# except IndexError:
#     print(f"Ro'yxatda {len(fruit)} ta meva bor!")



# KeyError
# user = {
#     'username': 'usmonnosirov',
#     'status': 'manager',
#     'gmail': 'usmonnosirov@gmail.com',
#     'phone': '998912345678'
# }
# try:
#     print(f"Foydalanuvchi: {user['nomi']}")
# except KeyError:
#     print("Bunday kalit mavjud emas!")


# FileNotFoundError
# file = 'data.txt'
# try:
#     f = open(file)
# except FileNotFoundError:
#     print(f"{file} fayli mavjud emas!")


# BIR NECHTA XATOLIKLAR BILAN USHLASH:
a = input("Son kiriting: ")
try:
    a = int(a)
    b = 20 / a
except ValueError: # Agar foydalanuvchi butun son kiritsa
    print("Butun son kiritmadingiz.")
except ZeroDivisionError: # Agar foydalanuvchi 0 kiritsa
    print("0 ga bo'lib bo'lmaydi")
else:
    print(f"A: {a}")