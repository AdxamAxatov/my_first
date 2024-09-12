# class Hello:
#     def __init__(self, model, color, year, made):
#         self.model = model
#         self.color = color
#         self.year = year
#         self.made = made

#     def info(self):
#         information = f"Car model: {self.model}, color: {self.color}, year: {self.year}"
#         information += f", made by: {self.made}" 
#         return information 
    
# # user = Hello('BMW', 'black', 1984, 'China')
# # print(f'{user.info()}')

# class Mercedez(Hello):
#     def __init__(self, model, color, year, made):
#         super().__init__(model, color, year, made)

# user1 = Mercedez('BMW', 'black', 1984, 'China',)
# print(f'{user1.info()}')


# no1

# class Odam:
#     def __init__(self, name, surname, year):
#         self.name = name
#         self.surname = surname
#         self.year = year

#     def get_info(self):
#         return f"{self.name} {self.surname}"
    
#     def get_age(self, year):
#         return year - self.year
    
# person = Odam('Adxam', 'Axatov', 2006)
# print(f"{person.get_info()} {person.get_age(2024)} year old")


# class Teacher(Odam):
#     def __init__(self, name, surname, year):
#         super().__init__(name, surname, year)

# teacher = Teacher('John', 'Wick', 1985)
# print(f"{teacher.get_info()} {teacher.get_age(2024)} year old")


# class Student(Odam):
#     def __init__(self, name, surname, year):
#         super().__init__(name, surname, year)

# student = Student('Carl', 'Johnson', 2002)
# print(f"{student.get_info()} {student.get_age(2024)} year old")































