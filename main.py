# from random import randint
# '''
# Задача 22: Даны два неупорядоченных набора целых чисел (может быть, с повторениями). Выдать без повторений в порядке возрастания все те числа,
#  которые встречаются в обоих наборах.Пользователь вводит 2 числа. n — кол-во элементов первого множества. m — кол-во элементов второго множества.
#  Затем пользователь вводит сами элементы множеств.
# '''
#
# size_sp1 = int(input("Введите размер первого списка "))
# sp = [size_sp1]
# for i in range(size_sp1):
#     sp.append(randint(1, 10))
# size_sp2 = int(input("Введите размер второго списка "))
# sp2 = [size_sp2]
# for i in range(size_sp2):
#     sp2.append(randint(1, 10))
# print (sp)
# print(sp2)
# sp3 = []
# for i in sp:
#     for j in sp2:
#         if i not in sp3:
#             if i == j:
#                 sp3.append(i)
#
# print(sorted(sp3))
#
