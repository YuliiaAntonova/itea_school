# 1. Программа принимает от пользователя диапазоны для коэффициентов
# a, b, c квадратного уравнения: ax2 + bx + c = 0. Перебирает все варианты целочисленных
# коэффициентов в указанных диапазонах, определяет квадратные уравнения, которые имею решение

from random import randint

N = 10
M = 10
matrix = []
for i in range(N):
    row = []
    for j in range(M):
        row.append(randint(0, 20))
    matrix.append(row)
for row in matrix:
    for item in row:
        print("% 4d" % item, end='')
    print()
num = int(input("Искоемое число: "))
for i in range(N):
    for j in range(M):
        if num == matrix[i][j]:
            print(f"[{i}, {j}]")



