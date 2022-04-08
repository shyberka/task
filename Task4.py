from math import*

a = int(input('Введите угол альфа(в градусах): '))

s = radians(sin(a))
c = radians(cos(a))
tg = radians(tan(a))
ctg = radians(c/s)

print('синус: ', s)
print('косинус: ', c)
print('тангенс: ', tg)
print('катангенс: ', ctg)