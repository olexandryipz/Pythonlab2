n = int(input("Введіть число n: "))

for i in range(1, 100):
    square = i**2
    if square > n:
        print("Перше число більше n:", square)
        break
