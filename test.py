
#task10

n = int(input('введите кол-во монеток: '))
a = 0
for i in range(n):
    b = int(input('Введите монетки: '))
    if b == 1:
        a += 1
if a < n/2:
    print(a)
else :
    print(n - a)


#task12

from math import sqrt

def calculate(b, c):
    D = b*b + 4*c
    if D > 0:
        sq = sqrt(D)/2
        p = b/2
        x1 = p-sq
        x2 = p+sq
        return [x1, x2]

def main():
    b = int(input('Введите сумму чисел: '))
    c = -int(input('Введите произведение чисел: '))
    print(calculate(b, c))
main()


#task14

a = int(input('Введите число: '))
sum = 0
k = 1
while k < a:
    k *= 2
    sum += 1
    print(sum, end= ' ')
if a < 0:
    print('неверное число')

