import math

a = float(input("Введіть перше число: "))
b = float(input("Введіть друге число: "))
c = float(input("Введіть третє число: "))
d = float(input("Введіть четверте число: "))

min_value = min(a, b, c, d)
cos_min = math.cos(min_value)

print(f"Косинус мінімального числа ({min_value}): {cos_min}")