# 'w' - write
# 'r' - read
# 'a' - append

# with open('pi.txt', '') as f:
#     pi = f.read()
#     print(pi)


# file = open('pi.txt')
# pi1 = file.read()
# print(pi1)
# file.close()



# with open('pi.txt') as f:
#     pi = f.read()
#     pi = pi.rstrip()
#     pi = pi.replace('\n', '')
#     pi = float(pi)
#     print(type(pi))


# with open('D:\Softwares//Tramplin-Backends\Group-1//pi.txt', 'r') as f:
#     pi = f.read()
#     print(pi)


# filenomi = 'pi.txt'
# with open(filenomi, 'r') as f:
#     for line in f:
#         print(line)


with open('names.txt') as f:
    students = f.readlines()
    print(students)

students = [i.rstrip() for i in students]
print(students)















