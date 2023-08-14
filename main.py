# HOMEWORK 08/08/2023

# TASK 30

# a1 = int(input('Введите первый элемент: '))
# d = int(input('Введите шаг : '))
# k = int(input('Введите количество элементов: '))
# result = []
# for i in range(k):
#     result.append(a1+i*d)
# print(result)

# TASK 32
# data = [rd(1, 100) for i in range(10)]
# print(data)
# res = []
# a = int(input("Введите начало диапазона: "))
# b = int(input("Введите окончание диапазона: "))
# for i in range(len(data)):
#     if data[i] >= a and data[i] <= b:
#         res.append(i)
# print(res)



# def transformation(value):
#     return value
# transformation = lambda value : value


# values = [1, 4, 23, 'asfdk']
# transformed_values = list(map(transformation, values))
# if values == transformed_values:
#     print('ok')
# else:
#     print('fail')
# # transformation = lambda(map)
# def transformation(value):
#     return value

# def square(x, y):
#     return x * y
# volume = lambda x, y, z: x * y * z
# print(volume(5, 2, 4))

# TASK 49
# orbits = [(1, 3), (2.5, 10), (7, 2), (6, 6), (4, 3)]
# max_orbits = orbits[0]
# max_s = 0
# for orbit in orbits:
#     print(orbit)
#     # a, b = elem[0], elem[1]
#     a, b = orbit
#     print(a * b)
#     S = a * b
#     if S > max_s and a != b:
#         max_s = S
#         max_orbits = orbit
# print(max_s, max_orbits)

# HOMEWORK

# TASK 34

# def krichalka(str):
#     str = str.split()
#     data = []
#     for word in str:
#         sum = 0
#         for i in word:
#             if i in 'аеёиоуыэюя':
#                 sum += 1
#         data.append(sum)
#     return len(data) == data.count(data[0])
# phrase = 'пара-ра-рам рам-пам-папам па-ра'
# if krichalka(phrase):
#     print('Парам пам-пам')
# else:
#     print('Пам парам')


# TASK 36

def print_operation_table(operation, num_rows=6, num_columns=6):
    a = [[operation(i, j) for j in range(1, num_columns + 1)] for i in range(1, num_rows + 1)]
    for i in a:
        print(*[f"{x:>3}" for x in i])


print_operation_table(lambda x, y: x * y)