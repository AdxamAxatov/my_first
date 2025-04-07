# for:
# Iterable: str, list, tuple, set, dictionary.

# ismlar = ['zilola', 'sherzod', 'alisher', 'qosim', 'maksim', 'sakina']
# for ism in ismlar:
#     for i in ism:
#         print(i)
#     print(ism)



# ismlar = ['zilola', 'sherzod', 'alisher', 'qosim', 'maksim', 'sakina']
# for i in ismlar:
#     print(i.capitalize())
#     print(i.upper())

# ( , , )
# numbers = list(range(11))
# sonlar = []
# # print(numbers)
# for i in numbers:
#     sonlar.append(i)
#     # sonlar.extend(i) # Xatolik qaytaradi.
# print(numbers)
# print(sonlar)


cars = []
for i in range(int(input("Nechta mashina kiritishni xohlaysiz?"))):
    cars.append(input(f"{i+1}-mashinani kiriting: "))
print(cars)


# for i in range(int(input(">>> "))):
#     print("Sherzod")


for i in range(1, int(input(">>> "))+1):
    print(i, end=' ')


