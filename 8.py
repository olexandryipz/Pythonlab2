numbers = [float(input("Введіть число: ")) for _ in range(3)]

positive_count = sum(1 for num in numbers if num > 0)
print("Кількість позитивних чисел:", positive_count)
