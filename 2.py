year = int(input("Введіть номер року: "))

if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
    print("У цьому році 366 днів (високосний).")
else:
    print("У цьому році 365 днів.")
