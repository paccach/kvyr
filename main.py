from math import sqrt

print('ax^2 + bx + c = 0')
a = float(input('a = '))
b = float(input('b = '))
c = float(input('c = '))
D = b * b - (4 * a * c)
if D < 0:
    print('уравнение не имеет корней')
elif D == 0:
    x = -b / (2 * a)
    print('уравнение имеет один корень: ', x)
else:
    x1 = (-b + sqrt(D)) / (2 * a)
    x2 = (-b - sqrt(D)) / (2 * a)
    print('уравнение имеет два корня: ', x1, ' ', x2)
