
# f = open('info.txt', 'r')
# # print(f.split(","))
#
# while True:
#     # считываем строку
#     line = f.readline()
#     # прерываем цикл, если строка пустая
#     if not line:
#         break
#     # выводим строку
#     print(line.strip().split(","))


f = open('info.txt', 'r')
# print(f.split(","))

line = f.read().split(",")

print(line)

id=0
# while len(line)>id:
#     id=id+4
#     print(line[id])




# while True:
#     # считываем строку
#     line = f.readline()
#
#     # прерываем цикл, если строка пустая
#     if not line:
#         break
#     # выводим строку
#     print(line.strip().split(","))


