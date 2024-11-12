months = {
    1: "January", 2: "February", 3: "March", 4: "April",
    5: "May", 6: "June", 7: "July", 8: "August",
    9: "September", 10: "October", 11: "November", 12: "December"
}

month_num = int(input("Введіть номер місяця (1-12): "))

if 1 <= month_num <= 12:
    print("Місяць англійською:", months[month_num])
else:
    print("Неправильний номер місяця.")