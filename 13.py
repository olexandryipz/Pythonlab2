a = int(input("Введіть число a: "))

sum_of_squares = sum(i**2 for i in range(a, 51))
print("Сума квадратів від a до 50:", sum_of_squares)
