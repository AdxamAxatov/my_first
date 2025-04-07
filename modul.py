def autoInfo(made, model, color, engine, year, price=None):
    auto = {
        "kompaniya": made,
        'model': model,
        'rangi': color,
        'korobka': engine,
        'yili': year,
        'narxi': price
    }
    return auto


def auto_kirit():
    while True:
        cars = []
        print("Quyidagi ma'lumotlarni kiriting: ")
        kompaniya = input("Ishlab chiqaruvchi kompaniya: ")
        model = input("Modeli: ")
        rangi = input("Rangi: ")
        korobka = input("Korobkasi: ")
        yili = input("Ishlab chiqarilgan yili: ")
        narxi  = input("Narxi: ")
        cars.append(autoInfo(kompaniya, model, rangi, korobka, yili, narxi))

        javob = input("Yana avtomobil qo'shasizmi? (yes/no)")
        if javob == 'no':
            break
    return cars


def info_cars(autoInfo):
    print(f"{autoInfo['kompaniya'].title()} "
          f"{autoInfo['model']}, "
          f"{autoInfo['rangi'].title()}, "
          f"{autoInfo['korobka']}, "
          f"{autoInfo['yili']}-yil, ${autoInfo['narxi']}")



def darajani_hisoblovchi(a, b):
    return a**b


