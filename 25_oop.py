# OOP - Object Oriented Programming - Obyektga yo'naltirilgan dasturlash

# OOPning tortta tamoyili mavjud:
# 1. Inkapsulatsiya;
# 2. Abstraktsiya;
# 3. Vorislik - Inheritance ota yoki super class deyiladi;
# 4. Polimorfizm.

# x = 10
# print(type(x))

# def salom():
#     print("AssalomU ALAYKUM!")

class Student:
    """Student nomli class yaratamiz"""
    def __init__(self, ism, familiya, tyil):
        self.ism = ism
        self.familiya = familiya
        self.tyil = tyil

    def info(self):
        print(f"{self.ism} {self.familiya} {self.tyil}")

talaba1 = Student('adxam', 'diyorbekov', 2024)
# print(talaba1.ism)
# print(talaba1.familiya)
# print(talaba1.tyil)

# talaba1.info()


# class Car:
#     """Car nomli class yaratamiz"""
#     def __init__(self, made: str, model: str, color, year):
#         self.made = made
#         self.model = model
#         self.color = color
#         self.year = year

#     def info(self):
#         print(f"Men bugun {self.made.upper()} {self.model.upper()} sotib oldim. Yili: {self.year}")

#     def buy_car(self):
#         pass

#     def remove(self):
#         pass

#     def list(self):
#         pass

#     def sort_from_up_to_low(self):
#         pass

#     def kattadan_kichikka(self):
#         pass

# mashina1 = Car('hummer', 'h2', 'sariq', 2020)
# mashina1.info()



# a = 10
# b = 10

# print(id(a))
# print(id(b))

# int = -5 dan 256 gacha memory optimization



# float type 16 xonali sonlargacha hisoblay oladi. Uyog'iga o'zi taxmin qilib yuboradi.
# 1.1234567891012131
from decimal import Decimal
print(Decimal(19)/Decimal(155)*Decimal(155)/Decimal(19))



# 1. Kiritilgan qiymatlar ichida birinchi harfini takrorlanganini $ belgisi bilan o'zgartirib qo'ying;
# 2. 123 -> 321;
# 3. 123 - > 213;
# 4. Musbat va manfiy sonlarni bir qatorda yozilgan dastur orqali natijani chiqaring;
# 5. string = X-DSPAM-Confidence: 0.8475 -> 0.8475;
# 6. User kiritgan faqat unli harflarni boshqa o'zgaruvchiga o'zlashtiring;
# 7. User kiritgan qiymatlar ichidan faqat unli harflar o'rniga # belgisi bilan o'zgartiruvchi dastur yozing;
# 8. Kartadagi oxirgi 4 ta raqamini ko'rinib, qolgan raqamlar o'rniga * qo'ying:  **** **** **** 1234









