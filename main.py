n = int(input("Введите количество монет: "))
count_reshka = 0
count_orel = 0
for i in range(n):
    i = int(input("Определите сторону монеток. отрицательные = решка, положительные(от ноля) = орел. Бросайте "))
    if i < 0:
        count_reshka += 1
    elif i > 0:
        count_orel += 1
if count_orel >= count_reshka:
    print(count_reshka)
else:
    print(count_orel)