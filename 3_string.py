# STRING(str) - MATNLAR USTIDA AMALLAR:
# ism = 'Umar'
# print("Mening ismim", ism)
# print("Mening ismim"+ ism)

# print(end="")
# print("Hello")

# '\n'
# '\t'

# ism = "Umar"
# familiya = 'Kadirov'

# print(ism, familiya)
# print(ism +" "+ familiya)

# f-string
# ism = 'lola'
# familiya = 'Kadirova'

# ism_sharifi = f"{ism} {familiya}"
# print(ism_sharifi)

# first_name = "Michael"
# last_name = "Jackson"
# print(f"Mening ismim {first_name} {last_name}. Yoshim esa {2024-2007} da")


# tyil = 2002
# print(f"Siz {tyil}-yilda tug'ilgansiz")
# print(f"Siz {2024-tyil}-yoshdasiz")



# MATNLAR BILAN ISHLASH(METODALAR):
# ism = 'sherzod'
# familiya = 'ABRORov'
# ism_sharifi = f"{ism} {familiya}"
# print(ism_sharifi.title())
# print(ism_sharifi.capitalize())
# print(ism_sharifi.upper())
# print(ism_sharifi.lower())



# strip(), rstip, lstrip()
meva = "    lemon   "
# print(f"Men {meva} sotib oldim")
print(f"Men {meva.strip()} sotib oldim")
# print(f"Men {meva.rstrip()} sotib oldim")
# print(f"Men {meva.lstrip()} sotib oldim")
kocha = ""
kucha = ""


# viloyat = "jizzax".title()
# viloyat = "jizzax"
# tuman = 'zomin'
# mahalla = 'ziyolilar'
# kocha = 'havaskorlar'
# print(f"{viloyat.title()} viloyati\n"
#       f"{tuman.title()} tumani\n"
#       f"{mahalla.title()} mahallasi\n"
#       f"{kocha.title()} ko'chasi")



# ozgaruvchilar = "Hello world"
# print(ozgaruvchilar[-1])
# len() - length
# print(len(ozgaruvchilar))


# in
# text = "Usmon Westminsterda ;ljljkhkjgrantdfgdfgfdg asosida o'qishga taklif etildi"
# print("gran" in text)
# print("gran" not in text)

var = "Salom Sherzod"
#print(var[0], end="")
#print(var[1], end="")
#print(var[2], end="")
#print(var[3], end="")
#print(var[4], end="")

# [Start:End: Step]
# [Boshlanishi:Tugashi: Qadami]

# print(var[0:5])
# print(var[:5])
# print(var[2:])

# replace()
ism = "Otajon"
print(ism.replace('j', '1'))

# format()
# yosh = 24
# matn = "Mening ismim Jackson. Mening yoshim {}"
# print(matn.format(yosh))


# moshina = "Mercedes Benz"
# narxi = 80_000
# # narxi = 800000
# modeli = "Gelik"
# buyurtma = "Sherzod {} sotib oldi. Narxi {}. Modeli esa {} ekan."
# print(buyurtma.format(modeli, narxi, moshina))


# isnumeric()
# son = "15145245"
# son1 = "25841h541542"
# num = son.isnumeric()
# num1 = son1.isnumeric()
# print(num)
# print(num1)

# isdigit()
# num2 = son.isdigit()
# print(num2)

# isaplha()
text = "Google"
#print(text.isalpha())


# index()
top = "Mening ismim Otajon. Yaxshimisizlar?"
b = top.index("Otajon")
# print(b)

# find()
b = top.find('Otajon')
# print(b)


# count()
# xat = "Adxamning uchta iphone telefoni bor. Bittasini do'stiga iphone sovg'a qildi. Do'stida ham iphone bor. B"
# sovga = xat.count("a")
# print(sovga)


# casefold()
# maktub = "Usmon bugun ARMIYAGA ketayapti"
# x = maktub.casefold()
# print(x)
