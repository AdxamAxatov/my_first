# lambda argument: ifoda


# daraja = lambda a, b: a ** b
# print(daraja(a=int(input("A: ")), b=int(input("B: "))))

# def daraja(n):
#     return lambda x: x**n

# kvadrat = daraja(2)
# kub = daraja(3)

# print(f"2-ning kvadrati: {kvadrat(2)} ga teng")
# print(f"3-ning kvadrati: {kub(3)} ga teng")





# from math import sqrt

# numbers = list(range(11))
# ildizlar = list(map(sqrt, numbers))
# print(ildizlar)



# a = int(input("A: "))
# b = int(input("B: "))
# a, b = map(int, input().split())
# print(a + b)


# number = list(range(11))
# def daraja(n):
#     return n * n

# print(list(map(daraja, number)))




# number = list(range(11))
# kv = list(map(lambda a: a*a, number))
# print(kv)



# number = list(range(11))
# kvadratlar = []
# for i in number:
#     kvadratlar.append(i*i)

# print(kvadratlar)


# birinchi = [1,2,3]
# ikkinchi = [4,5,6]
# uchinchi = list(map(lambda i, o: i + o, birinchi, ikkinchi))
# print(uchinchi)


# names = ['sherzod', 'zilola', 'usmon']
# print(list(map(lambda i: i.upper(), names)))



# import random as r
# sonlar = r.sample(range(100), 10)

# def juft(x):
#     return x % 2 == 0

# juft_sonlar = list(filter(juft, sonlar))
# print(sonlar)
# print(juft_sonlar)



# ismlar = ['usmon', 'adxam', 'diyorbek', 'umar', 'ali']
# ism = list(filter(lambda a: a.startswith('um'), ismlar))
# print(ism)

# ismlar = ['usmon', 'adxam', 'diyorbek', 'umar', 'ali']
# name = list(filter(lambda a:len(a) <= 4, ismlar))
# print(name)



def teskari(son):
    if son == 0:
        return
    print(son, end=" ")
    teskari(son - 1)

def togri(son):
    if son == 0:
        return
    togri(son - 1)
    print(son, end=" ")


teskari(5)
print()
togri(5)



