n = int(input("Введіть число n: "))

current = 1
i = 1
while current <= n:
    current += i
    i += 2
print("Перше число більше n:", current)
