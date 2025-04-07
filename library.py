# Library - Kutubxonalar

# datetime
# math

# import datetime as dt
# hozir = dt.datetime.now()
# print(hozir)
# print(hozir.date())
# print(hozir.time())
# print(hozir.hour)
# print(hozir.minute)
# print(hozir.second)

# bugun = dt.datetime.today()
# print(bugun)

# ertaga = dt.date(2024, 9, 3)
# print(ertaga)


# hozir = dt.datetime.now()
# thistime = hozir.time()
# print(f"Hozir soat: {thistime}")


# keyingivaqt = dt.time(15,44,55 )
# print(keyingivaqt)

# bugun = dt.date.today()
# ramazon = dt.date(2025, 4, 15)
# farq = ramazon-bugun
# print(f"Ramazonga {farq.days} kun qoldi!")


# hozir = dt.datetime.now()
# soccer = dt.datetime(2025, 3, 10, 23, 45, 00)
# farq = soccer-hozir
# sekundlar = farq.seconds
# minutlar = int(sekundlar / 60)
# soatlar = int(minutlar / 60)
# print(f"Futbol boshlanishiga {farq.days} kunu {soatlar} soat qoldi!")

# strftime()
# hozir = dt.datetime.now()
# vaqt = hozir.strftime("%H:%M:%S")
# print(f"Hozir soat: {vaqt}")


# strftime()
# hozir = dt.datetime.now()
# sana = hozir.strftime("%d-%m-%Y")
# print(f"Bugun sana: {sana}")

# hozir = dt.datetime.now()
# sana_vaqt = hozir.strftime("%d-%m-%Y, %H:%M:%S")
# print(sana_vaqt)


# math
# import math
# 4.5 = 5
# 4.6 = 5
# 4.4 = 4
# n = 4.5
# print(math.ceil(n))
# print(math.floor(n))

# E = math.e # e - Natural logarifm asosi
# print(E)


# pip install googletrans==3.1.0a0
from googletrans import Translator

tarjimon = Translator()
matn_uz = input("Matn kiriting: ")
tarjima = tarjimon.translate(matn_uz)
print(tarjima.text)

# import datetime as dt
# a = dt.datetime.now()
# print(a)
