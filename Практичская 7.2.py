n=int(input("Введите количество элементов: "))
a=list(map(int,input("Введите элементы").split()))
p_a=[x for x in a if x>0]
other_a=[x for x in a if x <=0]
print("Положительные элементы:", p_a)
print("Остальные элементы:", other_a)