# class Talaba:
#     def __init__(self, ismi, familiya, tyil):
#         self.ismi = ismi
#         self.familiya = familiya
#         self.tyil = tyil
#         self.bosqich = 1
    
#     def info(self):
#         return f"{self.ismi} {self.familiya}. {self.bosqich}-bosqich talabasi."
    
#     def update_bosqich(self):
#         self.bosqich += 1

# talaba1 = Talaba('Zubayir', 'Akobirov', 1999)
# print(talaba1.info())

# talaba1.update_bosqich()
# talaba1.update_bosqich()
# print(talaba1.info())


# class Lesson:
#     def __init__(self, nomi):
#         self.nomi = nomi
#         self.talabalar_soni = 0
#         self.talabalar = []

#     def add_talabalar(self, talaba):
#         self.talabalar.append(talaba)
#         self.talabalar_soni += 1

#     def info(self):
#         return [i.info() for i in self.talabalar]

# software = Lesson("Dasturlash")
# english = Lesson("English")

# talaba1 = Talaba('Zubayir', 'Akobirov', 1999)
# talaba2 = Talaba('Diyorbek', 'Abullayev', 2005)
# talaba3 = Talaba('Adxam', 'Sobirov', 1998)
# talaba4 = Talaba('Usmon', 'Ibragimov', 1997)
# talaba5 = Talaba('Furqat', 'Alisherov', 2000)

# software.add_talabalar(talaba2)
# software.add_talabalar(talaba5)
# software.add_talabalar(talaba1)

# english.add_talabalar(talaba4)
# english.add_talabalar(talaba3)

# print(f"Software: {software.talabalar_soni}")
# print(f"English: {english.talabalar_soni}")

# print(software.talabalar)
# print(english.talabalar)

# print(software.info())
# print(english.info())

# soft = software.info()
# eng = english.info()
# print(soft)
# print(eng)



# SET va GET
class Talaba:
    """Ushbu class Talabaning bir nimasini ishlab chiquvchi class"""
    def __init__(self, ismi, familiya):
        self.ismi = ismi
        self.familiya = familiya
        self.kurs = 1
    
    def set_kurs(self, kurs):
        self.kurs = kurs
    
    def update_kurs(self):
        self.kurs += 1

    def get_info(self):
        return f"{self.ismi} {self.familiya}. {self.kurs}-bosqich talbasi."

    def get_name(self):
        return self.ismi

    def get_familiya(self):
        return self.familiya


class Lesson:
    def __init__(self, nomi) -> None:
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_talabalar(self, talaba):
        self.talabalar.append(talaba)
        self.talabalar_soni += 1

    def get_nomi(self):
        return self.nomi
    
    def get_talabalar(self):
        return [i.info() for i in self.talabalar]
    def get_talabalar_soni(self):
        return self.talabalar_soni

talaba1 = Talaba("Adxam", "Usmonov")
print(talaba1.get_info())
talaba1.update_kurs()
print(talaba1.get_info())

talaba2 = Talaba("Diyorbek", "Furqatov")
talaba2.set_kurs(3)
print(talaba2.get_info())
talaba2.update_kurs()
print(talaba2.get_info())

