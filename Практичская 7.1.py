n=int(input("Введите количество элементов"))
a=list(map(int,input("Введите элементы:").split()))
min_value=min(a)
min_index=a.index(min_value)
print(f"Минимальый элемент: {min_value}")
print(f"Индекс минимального элемента: {min_index}")