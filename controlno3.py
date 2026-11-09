a = int(input())
b = int(input())


if a > b:
    temp = a
    a = b
    b = temp

izobilni_broi = 0
namera_li_savarsheno = False

for i in range(a, b + 1):
    suma = 0
    for d in range(1, i):
        if i % d == 0:
            suma += d
            
    if suma == i:
        print(i, end=" ")
        namera_li_savarsheno = True
    if suma > i:
        izobilni_broi += 1
        
if not namera_li_savarsheno:
    print("Няма")
else:
    print()  # Нов ред

print("Izobilni: ", izobilni_broi)