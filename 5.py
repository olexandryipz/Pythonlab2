import math

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))

max_value = max(a, b, c)
sin_max = math.sin(max_value)

print(f"Синус максимального числа ({max_value}): {sin_max}")