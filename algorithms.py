emails = []
client = []
products = []
while True:
    command = input('command: ').lower()
    if command == '/new':
        products.append({"name": input('mahsulot nomi: '),
                        'price': int(input('mahsulot narxi: ')),
                        'soni': int(input('mahsulot soni: ')),
                        'total': 0})
                        
        
    elif command == '/list':
        for i in products:
            print(f"{i['name']} {i['soni']} ta \n{i['price']} so'mdan")
        
    elif command == '/buy':
        users = {
            'product': input("sotib olmoqchi bo'lgan mahsulot nomi: ")
            }
        for o in products:
            if o['name'] == users['product']:
                client.append(users['product'])
                new = {
                    'buy_count': int(input('sotib olinuvchi mahsulot soni(hajmi): '))
                    }
                if new['buy_count'] <= o['soni']:
                    o['soni'] -= new['buy_count']
                    o['total'] +=  new['buy_count']
                    client.append(new['buy_count'])
                    for i in client:
                        # print(f'{i['product']} savatga solindi!\njami narxi: {i['buy_count']}')
                        print(i)
                else:
                    new >= o['soni']
                    print('sorry there is not enough products!')                 
          
    elif command == '/rasmiylashtirish':
        emails.append(input('email pochtangizni kirgazing: '))   
        print(client) 

    elif command == '/products':
         for i in client:
            # print(f'{i['product']} savatga solindi!\njami narxi: {i['buy_count']}')
            # need to make client variable dict to make code above work
            print(i)

    elif command == '/payment':
        print('tolov uslubini tanlang! ')

    elif command == '/remove':
        user = input("Savatdan o'chirilmoqchi bo'lgan mahsulot nomi: ").lower()
        for i in client:
            if i == user:
                client.remove(user)
                print('kritilgan mahsulot savatdan olindi!')

    elif command == '/exit':
        break


































