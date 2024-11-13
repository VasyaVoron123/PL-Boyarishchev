import math
a=float(input("Введите длину стороны шестиугольника:"))
def t_area(a):
    return(math.sqrt(3)/4)*a**2
def h_area(a):
    return 6*t_area(a)
print("Площадь шестиугольника:",h_area(a))