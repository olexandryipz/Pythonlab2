a = int(input("Введіть перше число A: "))
b = int(input("Введіть друге число B: "))

if a >= b:
    print("A повинно бути менше B")
else:
    squares_sum = 0
    for i in range(a, b + 1):
        squares_sum += i ** 2

    print(f"Сума квадратів всіх цілих чисел від {a} до {b}: {squares_sum}")