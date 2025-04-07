# QIYMAT QAYTARUVCHI FUNKSIYA:
# def salom(ism=25):
#     print(ism)

# salom(10)

# def ism_familiya(ism, familiya: str):
#     toliq_ismi = f"{ism} {familiya.title()}"
#     print(toliq_ismi)

# student1 = ism_familiya('adxam', 'usmonov')



# def ism_familiya(ism, familiya, otasining_ismi=""):
#     if otasining_ismi:
#         toliq_ismi = f"{ism} {familiya} {otasining_ismi}"
#     else:
#         toliq_ismi = f"{ism} {familiya}"
#     return toliq_ismi


# ism_familiya('usmon', 'diyorbekov')
# print(ism_familiya('sherzod', 'adxamov', 'ulug\'bek o\'g\'li'))
# print(ism_familiya('sherzod', 'adxamov'))




# def daraja(a, b):
#     return a ** b

# print(daraja(5, 5))
# daraja(5, 5)


# ----------------------------------------------------------------
# def auto_info(made, model, color, engine, year, price=None):
#     auto = {
#         'Company': made,
#         'Model': model,
#         'Color': color,
#         'Engine': engine,
#         'Year': year,
#         'Price': price
#     }
#     return auto

# car1 = auto_info("GM", "Malibu 2", 'qora', 'automatic', 2024)
# car2 = auto_info("Mercedes", "220", 'qora', 'automatic', 2022)
# car3 = auto_info("Corvette", "C8", 'oq', 'automatic', 2024, 42_000)

# cars = [car1, car2, car3]
# for i in cars:
#     if i['Price']:
#         price = i['Price']
#     else:
#         price = "Nomalum"
#     print(f"{i['Company']} {i['Model']}. Rangi {i['Color']}. Narxi: {price}")
# ------------------------------------------------------------------------------------------------


# for i in car1.values():
#     print(i)
# print(car1)





# car = []
# while True:
#     made = input("Ishlab chiqargan kompaniya: ")
#     model = input("Modeli: ")
#     color = input("Rangi: ")
#     year = int(input("Yili: "))
#     price = int(input("Narxi: "))

#     car.append(auto_info(made, model, color, year, price))
#     answer = input("Yana mashina kiritasizmi: (yes/no): ")
#     if answer == "no":
#         break
# print(car)




# def masofa(min, max):
#     numbers = []
#     while min < max:
#         numbers.append(min)
#         min += 1
#     return numbers

# print(masofa(0, 11))




def oraliq(min, max, qadam=''):
    sonlar = []
    while min < max:
        sonlar.append(min)
        min += qadam
    return sonlar

print(oraliq(0, 10, 2))














