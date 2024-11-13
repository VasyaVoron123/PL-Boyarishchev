def rectangle_area(a, b):
    return a * b
areas = []
for i in range(1, 4):
    a = float(input(f"Введите первую сторону прямоугольника {i}: "))
    b = float(input(f"Введите вторую сторону прямоугольника {i}: "))
    areas.append(rectangle_area(a, b))
for i, area in enumerate(areas, 1):
    print(f"Площадь прямоугольника {i}: {area}")
