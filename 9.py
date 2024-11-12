a = int(input("Введіть перше число A: "))
b = int(input("Введіть друге число B: "))

if a >= b:
    print("A повинно бути менше B")
else:
    total_sum = 0
    for i in range(a, b + 1):
        total_sum += i

    print(f"Сума всіх цілих чисел від {a} до {b}: {total_sum}")