from SimpleIterationMethod import SolvingSoLE
from Matrix import Matrix
import random


def to_fixed(num, digits=0):
    return f"{num:.{digits}f}"


def print_matrix(matrix, count):
    for i in range(matrix.n):
        for j in range(matrix.n + 1):
            print(float(to_fixed(matrix.values[i][j], count)), end=" ")
        print()


def do(n, values, e, max_it):
    matrix = Matrix(values, n)
    simple = SolvingSoLE(matrix, e, max_it)
    check = simple.simple_iteration_method()
    if check:
        count = len(str(e)) - 2
        if "e" in str(e):
            count = int(str(e)[str(e).index("e")+2:])
        print("Вы ввели матрицу: ")
        print_matrix(matrix, count)
        print("Точнось: ")
        print(e)
        print("Было сделано итераций: ")
        print(simple.it)
        print("Вектор решения:")
        for i in range(len(simple.answer)):
            a = float(to_fixed(simple.answer[i], count))
            print("X_%i = %a" % (i+1, a))
        print("Вектор погрешности:")
        for i in range(len(simple.error)):
            a = simple.error[i]
            print("X_%d(%d) - X_%d(%d) = %a" % (i+1, simple.it, i, simple.it - 1, a))
    else:
        stop = True
        for i in range(n):
            for j in range(n + 1):
                if values[i][j] != 0:
                    stop = False
                    print("К сожалению, метод простой итерации тут бессилен")
                    break
            if not stop:
                break
        if stop:
            print("Бесконечно много решений, но это не метод простых итераций)")



def input_int():
    try:
        n = int(input())
        return n
    except ValueError:
        print("Вы ввели не число, попробуйте еще раз")
        return "*"


def input_float():
    try:
        e = float(input().replace(',', '.'))
        return e
    except ValueError:
        print("Вы ввели не число, попробуйте еще раз")
        return "*"


def input_matrix(values, n, count):
    try:
        for i in range(count):
            values.append([float(j) for j in input().split()])
            if len(values[i]) != n + 1:
                print("Вы ввели неправильные значения, попробуйте еще раз только последнюю строку")
                break
    except ValueError:
        print("Вы ввели неправильные значения, попробуйте еще раз только последнюю строку")


def console_input():
    print("Введите количество неизветных: ")
    n = input_int()
    while n == "*":
        n = input_int()
    print("Введите значения матрицы: ")
    values = []
    input_matrix(values, n, n)
    while len(values) != n:
        values = values[:len(values) - 1]
        input_matrix(values, n, n - len(values))
    print("Введите максимальное количество итераций: ")
    max_it = input_int()
    while max_it == "*":
        max_it = input_int()
    print("Введите точность: ")
    e = input_float()
    while e == "*":
        e = input_float()
    do(n, values, e, max_it)


def random_input():
    print("Введите количество неизветных: ")
    n = input_int()
    while n == "*":
        n = input_int()
    print("Введите максимальное количество итераций: ")
    max_it = input_int()
    while max_it == "*":
        max_it = input_int()
    print("Введите точность: ")
    e = input_float()
    while e == "*":
        e = input_float()
    values = []
    sum = 0 
    for i in range(n):
        str = []
        for j in range(n+1):
            str.append(random.uniform(1, 100))
            sum += abs(str[j])
        str[i] += sum
        values.append(str)
    print("Значения матрицы сгенерированны рандомно: ")
    do(n, values, e, 1000)


def file_input():
    try:
        f = open('input.txt', 'r')
        i = 0
        values = []
        n = 0
        max_it = 0
        e = 0.0
        for line in f:
            if i == 1:
                n = int(line)
            if i == 3:
                max_it = int(line)
            if i == 5:
                e = float(line)
            if i > 6:
                values.append([float(j) for j in line.split()])
            i += 1
        do(n, values, e, max_it)
    except ValueError:
        print("Что-то не так в файлике, проверьте данные")


print("Выберите способ ввода (1 - из консоли, 2 - рандомно, 3 - из файла)")
stop = False
while not stop:
    i = input()
    stop = True
    if i == "1":
        console_input()
    elif i == "2":
        random_input()
    elif i == "3":
        file_input()
    else:
        stop = False
