# dir()
# class Worker:
#     pass
# print(dir(Worker))
# print(dir(str))


def search_methods(s_class):
    return [method for method in dir(s_class) if method.startswith('__') is False]

# print(search_methods(str))

class Lesson:
    def __init__(self, nomi) -> None:
        self.nomi = nomi
        self.talabalar_soni = 0
        self.talabalar = []

    def add_talabalar(self, talaba):
        self.talabalar_soni += 1
        self.talabalar.append(talaba)

    def info_students(self):
        return [talaba.info() for talaba in self.talabalar]

astronomy = Lesson("Astronomiya")

# print(search_methods(astronomy))
# print(search_methods(Lesson))


# print(astronomy.__dict__.keys())


class Person:
    def __init__(self,name, last_name, passport, year):
        self.name = name
        self.last_name = last_name
        self.passport = passport
        self.year = year

    def get_info(self):
        information = f"{self.name} {self.last_name} "
        information += f"Passport: {self.passport}, {self.year}-yilda tug'ilgan"
        return information

    def get_age(self, year):
        return year - self.year

# odam = Person("Ibrohim", "Alimov", "ABS1234567", 1999)
# print(f"{odam.get_info()}. {odam.get_age(2024)} yoshda!")

class Student(Person):
    def __init__(self, name, last_name, passport, year):
        super(Student, self).__init__(name, last_name, passport, year)


talaba1 = Student("Alisher", "Ibragimov", "FF 1234567", 1998)
print(talaba1.get_info())
print(talaba1.get_age(2024))
























