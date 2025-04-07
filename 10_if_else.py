# if
# elif - else if
# else

# son = int(input(">>> "))
# if son >= 5:
#     print(son)

# yosh = int(input(">>> "))
# if yosh <= 8:
#     print("Siz uchun bilet narxi bepul")
# else:
#     print("Siz uchun bilet narxi 65 000 so'm")


# a, b = 24, 45
# print("a > b") if a>b else print("a < b")

# a = 24
# b = 45
# if a > b:
#     print("a > b")
# else:
#     print("a < b")



# cars = ['malibu', 'captiva', 'traverse', 'jetour', 'byd', 'l9', 'lexus', 'BMW']
# for i in cars:
#     if i.lower() == 'bmw':
#     # if i == 'bmw':
#         print(i.upper())
#     else:
#         print(i.lower())




# ismlar = ['STEVE jobs', 'Elon MUsK', 'michael Jackson', 'Mike Tyson', 'AL KHORAZMY', 'ROBERT Keyosaki']
# for i in ismlar:
#     if i.lower() == 'al khorazmy':
#         print(i.title())
#     else:
#         print(i.lower())


# number = int(input(">>> "))
# if number > 0:
#     print("Musbat son")
# elif number < 0:
#     print("Manfiy son")
# # elif number == 0:
# #     print("Kiritgan son 0 edi")
# else:
#     print("Kiritgan son 0 edi")



kun = input("Kunni kiriting: ").lower()
# kun = input("Kunni kiriting: ")
yosh = int(input("Yoshingizni kiriting: "))

# if kun.lower() == 'juma' and (yosh <= 7 or yosh >= 65):
if kun == 'juma' and (yosh <= 7 or yosh >= 65):
    print("Siz uchun bilet bepul!")
# elif kun.lower() == 'juma' and (yosh > 7 and yosh <= 18):
elif kun == 'juma' and (yosh > 7 and yosh <= 18):
    print("Siz uchun bilet 25 000 so'm")
else:
    print("Bilet narxi 65 000 so'm")

