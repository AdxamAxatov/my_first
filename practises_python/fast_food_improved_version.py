# lst = []
# menu = {
#     "lavash":{
#         "mini lavash": 25_000,
#         "big lavash": 32_000,
#         'pishloqli lavash': 35_000,
#         'tovuqli lavash': 28_000,
#     },
#     "pizza":{
#         'danar pizza': 45_000,
#         'oddiy pizza': 35_000,
#         'qazili pizza': 45_000,
#         'peporoni pizza': 35_000,
#         },
#     "gamburger":{
#         'oddiy gamburger': 25_000,
#         'cheese burger': 25_000,
#         },
#     "ichimliklar":{
#         'cola': 20_000,
#         'fanta': 18_000,
#         'flavis': 18_000,
#         'sprite': 18_000,
#         'pepsi': 18_000,
#         },}
# javob = ''
# son = 0
# hisob = 0
# while True:
#     for i in menu:
#         print(f"{i.upper()}: ")
        

#     if javob == "no":
#         break

#     user = input('\nchoose the options: ')
#     if user in menu:
#         for k,v in menu[user].items():
#             print(f'{son+1}-{k.upper()}: {v}')
#             son += 1

#     users = input('\nchoose the food you would like to order: ').lower()
#     if users in menu[user]:
#         hisob += menu[user][users]
#         lst.append(users)
#     else:
#         print(f"{users} mavjud emas!")

#     javob = input("\nDo you want to order more? (yes/no) ").lower()
#     print(f"Buyurtmalar: {[i for i in lst]}".replace("[", '').replace("]", ""))
#     print(f"Hisob: {hisob} so'm.\n")
    

# NEW VERSION

# menu = {
#     "lavash":{
#         "mini lavash": 25_000,
#         "big lavash": 32_000,
#         'pishloqli lavash': 35_000,
#         'tovuqli lavash': 28_000,
#     },
#     "pizza":{
#         'danar pizza': 45_000,
#         'oddiy pizza': 35_000,
#         'qazili pizza': 45_000,
#         'peporoni pizza': 35_000,
#         },
#     "gamburger":{
#         'oddiy gamburger': 25_000,
#         'cheese burger': 25_000,
#         },
#     "ichimliklar":{
#         'cola': 20_000,
#         'fanta': 18_000,
#         'flavis': 18_000,
#         'sprite': 18_000,
#         'pepsi': 18_000,
#         },}
# javob = ''
# son = 0
# hisob = 0
# clients = {}
# for i in menu:
#     print(f"{i.upper()}:\n ")
#     son = 1
#     for k,v in menu[i].items():
#                print(f'{son+1}-{k.upper()}: {v}')
#                son += 1
# while True:
#     users = input('\nchoose the food you would like to order: ').lower()
#     for i in menu:
#             for k,v in menu[i].items():
#                 if users in k or v:
#                     clients[users] = menu[i][users]
#                     hisob += menu[i][users]
#     else:
#             if users in ['stop', 'exit']:
#                 for k,v in clients.items():
#                     print(f'{k.upper()}: {v}')
#                 print(f"Buyurtmalar: {[i for i in clients]}".replace("[", '').replace("]", ""))
#                 print(f"Hisob: {hisob} so'm.\n")
#                 break
#             else:
#                   print('bunday ovqat majud emas!')

               
            


class Lavash:
    def __init__(self, menu) -> None:
        self.menu = menu

    def display(self):
        for i in self.menu:
                print(f'{i.upper()}')
                for k,v in self.menu[i].items():
                    print(f'{k.upper()}: {v}')
    
    def user(self, user):
        user = input('order please: ') 
        if user in self.menu:
             print('wait for five to ten minutes, your order will be ready!')
        else:
             print('order is not available sorry!')
                 
    def order(self):
         self.display()
         self.user(user = input('order'))

lavash = Lavash({
            "lavash":{
                "mini lavash": 25_000,
                "big lavash": 32_000,
                'pishloqli lavash': 35_000,
                'tovuqli lavash': 28_000,
            },
            "pizza":{
                'danar pizza': 45_000,
                'oddiy pizza': 35_000,
                'qazili pizza': 45_000,
                'peporoni pizza': 35_000,
                },
            "gamburger":{
                'oddiy gamburger': 25_000,
                'cheese burger': 25_000,
                },
            "ichimliklar":{
                'cola': 20_000,
                'fanta': 18_000,
                'flavis': 18_000,
                'sprite': 18_000,
                'pepsi': 18_000,
                },}
)
lavash.order()
























