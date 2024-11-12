base = float(input("Введіть основу трикутника: "))
height = float(input("Введіть висоту трикутника: "))

area = 0.5 * base * height

if area % 2 == 0:
    print(f"Площа трикутника, поділена на 2: {area / 2}")
else:
    print("Не можу ділити на 2!")