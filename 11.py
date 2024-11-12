a = int(input("Введіть число a: "))
b = int(input("Введіть число b: "))

total_sum = sum(range(a, b + 1))
count = b - a + 1
average = total_sum / count
print("Середнє арифметичне:", average)
