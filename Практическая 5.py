a=int(input("Введите целое число не меньше двух"))
otvet=a
for b in range(2, int(a**0.5)+1):
    if a%b ==0:
        otvet=b
        break
print(otvet)
