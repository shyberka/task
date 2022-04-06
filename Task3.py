from math import*

n = int(input('Количество чисел: '))
c = 0
for i in range(n):
    a = int(input('Число: '))
    c = c + a
k = c/n

y = round(k, 2)
print(y)