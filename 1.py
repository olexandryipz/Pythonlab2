numbers = [int(input("Введіть перше число: ")),
           int(input("Введіть друге число: ")),
           int(input("Введіть третє число: "))]

in_range = [num for num in numbers if 1 <= num <= 3]
print("Числа в інтервалі 1, 3:", in_range)