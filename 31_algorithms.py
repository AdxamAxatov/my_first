# dict comprehension:
# isms = ["Ali", "Bobur", "John"]
# years = [1998, 1999, 2000]

# dct = {}
# for ism, year in zip(isms, years):
#     dct[ism] = year
# print(dct)

# Lambda orqali list ichidagi elementlarni kv.ga ko'paytirish va qoldiqsiz bo'lish:
# elements = [1,2,3,4,5,6,7,8,9]
# print(list(map(lambda x: x**2, elements)))
# print(list(filter(lambda x: x % 2 == 0, elements)))


# ----------------------------------------------------------------
# class Car:
#     def __init__(self,):
#         color = input("Avtomobil rangini kiriting: ")
#         model = input("Avtomobil modelini kiriting: ")
#         self.color = color
#         self.model = model

#     def print_car(self):
#         print(f"Model: {self.model}, Rangi: {self.color}")


# cars = []
# while True:
#     command = input("Buyruqni kiriting: ")
#     if command == "/new":
#         cars.append(Car())
#     elif command == "/list":
#         for i in cars:
#             i.print_car()
# ----------------------------------------------------------------

client = []
products = []

while True:
    command = input("Command: ").lower()
    
    if command == "/new":
        products.append(
            {
                "name": input("Mahsulot nomi: "),
                'price': int(input("Mahsulot narxi: ")),
                'count': int(input("Mahsulot soni: ")),
                'buy_count': 0,
                }
                )
        
    elif command == '/list':
        for product in products:
            print(f"{product['name']}, {product['price']}, {product['count']}")

    elif command == "/buy":
        mahsulot_nomi = input("Mahsulot nomi: ")
        for product in products:
            if product['name'] == mahsulot_nomi:
                mahsulot_count = int(input("Mahsulot soni: "))
                if product['count'] >= mahsulot_count:
                    product['count'] -= mahsulot_count
                    product['buy_count'] += mahsulot_count
                else:
                    print("Mahsulot yetarli emas!")

    elif command == "/sort":
        products = sorted(products, key=lambda x: x['price'])
        for product in products:
            print(f"{product['name']} - {product['price']} - {product['count']}")

    elif command == '/trend':
        products = sorted(products, key=lambda x:x['buy_count'], reverse=True)
        print(f"{product['name']} - {product['price']} - {product['count']}")
    
    elif command =='/remove':
        mahsulot_nomi = input("Mahsulot nomi: ")
        for product in products:
            if product['name'] == mahsulot_nomi:
                del products[products.index(product)]
                break
    
    elif command =='/exit':
        break









































