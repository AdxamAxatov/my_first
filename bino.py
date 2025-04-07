class Bino:
    def __init__(self, nomi, balandlik):
        self.nomi = nomi
        self.balandlik = balandlik
    
    def info(self):
        if self.balandlik >= 50:
            print(self.balandlik, self.nomi)

# b1 = Bino('Pizza', 20)
# b2 = Bino('Nest One', 65)
# b3 = Bino('Eifel tower', 50)
# b4 = Bino('Helton', 55)
# b5 = Bino('Burj Khalifa', 890)

# b1.info()
# b2.info()
# b3.info()
# b4.info()
# b5.info()


# lst = [b1, b2, b3, b4, b5]
# for i in lst:
#     i.info()

# lst = []
# for i in range(int(input("Nechta bino kiritasiz: "))):
#     obj = Bino(nomi=input("Bino nomini kiriting: "), 
#                 balandlik=int(input("Bino balandligini kiriting: ")))
#     lst.append(obj)

# for i in lst:
#     print(i.info())