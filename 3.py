amount = float(input("Введіть суму покупки в гривнях: "))

if amount > 1000:
    discount = 0.05
elif amount > 500:
    discount = 0.03
else:
    discount = 0.0

final_amount = amount * (1 - discount)
print(f"Вартість покупки з урахуванням знижки: {final_amount:.2f} грн")