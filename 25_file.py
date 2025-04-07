# 'r'
# with open('pi.txt') as f:

# 'r+' - fileni o'qish va yozish uchun ochish.
# 'a+' - filega ma'lumot qo'shish va o'qish uchun ishlatiladi
# 'a' - filega me'lumot qo'shish uchun ishlatiladi


# filenomi = 'teacher.txt'
# with open(filenomi, 'w') as f:
#     f.write("Usmon")


# ism = 'diyorbek'
# yosh = '18'
# with open('new_file.txt', 'w') as f:
#     f.write(ism)
#     f.write(yosh)

# with open('new_file.txt') as f:
    # print(f.read())


# ism = 'diyorbek'
# yosh = '18'
# with open('new_file.txt', 'w') as f:
#     f.write(f"Mening ismim {ism}\n")
#     f.write(yosh)


# with open('new_file.txt', 'a') as f:
#     f.write("\nAbbosjon\n")
#     f.write(str(2000))



# Pickle file yozish:
import pickle
student1 = {'ism':'diyorbek', 'yosh':18, 'yili': 2004}
student2 = {'ism':'usmon', 'yosh':30, 'yili': 1989}

with open('info.dat', 'wb') as f:
    pickle.dump(student1, f)
    pickle.dump(student2, f)



with open('info.dat', 'rb') as f:
    talaba1 = pickle.load(f)
    talaba2 = pickle.load(f)

print(talaba1)
print(talaba2)
