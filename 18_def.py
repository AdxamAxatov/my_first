# def narxini_kirit(nomi):
#     narxlari = {}
#     while nomi:
#         nom = nomi.pop()
#         summa = input(f"{nom.title()}ning narxini kiriting: ")
#         narxlari[nom] = summa
#     return narxlari

# cars = ["Ferrari", "Hummer2", "Cyber Truck", "Corvette", "Bugatti"]
# narxlari = narxini_kirit(cars[:])
# print(narxlari)
# print(cars)


# *args va **kwargs

# def summa(*numbers):
#     overall = 0
#     for i in numbers:
#         overall += i
#     return overall
# print(summa(1,2,3,4,5,6,7,8,9,10-1))


# def somma(*sonlar):
#     return sum(sonlar)

# print(somma(1,2,3,4,5,6,7,8,9))

# def info(a, b, *sonlar):
#     return a+b+sum(sonlar)

# print(info(5, 55, 25))
# print(info(-5, 5))



def autoInfo(company, model, **information):
    information['kompaniya'] = company
    information['Modeli'] = model
    return information

car1 = autoInfo("Rollse Royce", "Phantom", rangi='qora', year = 2024, price=25_000_000)
print(car1)









