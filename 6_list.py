# NON PREMITIVE:
# 1. List 
# 2. Tuple
# 3. Set
# 4. Dictionary

# son = 25
# son = int()

# LIST:
# mylst = []
# mylst = list()

# mylist = [1, 1.9, True, False, "Salom", 1, 0, None]
# print(type(mylist))

# son = "salom"

# mevalar = ['lemon', 'banan', 'qulupnay', 'malena', 'olma', 'olcha']
# narxi = [10_000, 15_000]
# sonlar = ['ikkita', 'bir kg', 5, 25, 30] # Aralash ro'yxat
# ismlari = [] #Bo'sh ro'yxat
# print(mevalar)
# print(narxi)
# print(sonlar)

# print("Men", mevalar[0].upper() + 'ni'.upper(), 'yaxshi ko\'raman')
# print("Men", mevalar[3].capitalize(), 'sotib oldim')
# print(len(mevalar)) # Listning uzunligini aniqlamoqchi bo'lsak

# print("Men bugun" + mevalar[-1], 'yemadim')

# print(narxi[0] + narxi[1])

# print(mevalar[-1])


sinf = ["zilola", 'ulug\'bek', 'usmon', "sherzod", 'adxam']
# print(*sinf)

# print(sinf[2:5])
# print(sinf[2:])



# mevalar = ['lemon', 'banan', 'qulupnay', 'malena', 'olma', 'olcha']
# print(mevalar)
# mevalar.append('kiwi')
# mevalar.append('nok')
# print(mevalar)


car = []
# print(car)
car.append('BYD')
car.append('BMW')
car.append('Mercedes Benz')
car.append('Le 9')
car.append('Rolls Royce')
car.append('Bugatti')
# print(car)


car.insert(0, "Ferrari")
# print(car)

# del() remove()
del car[1]
print(car)
car.remove("Bugatti")
print(car)

new = car.pop(2)
# new = car.pop()
print(new)
print(car)


# clear()
car.clear()
print(car)
