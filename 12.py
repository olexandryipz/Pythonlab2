a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

sum_result = 0
i = a
while i <= b:
    sum_result += i
    i += 1
print("Сума цілих чисел від a до b:", sum_result)
