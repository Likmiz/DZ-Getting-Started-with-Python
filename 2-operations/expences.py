food = float(input("Введите сумму расходов на еду: "))
transport = float(input("Введите сумму расходов на транспорт: "))
entertainment = float(input("Введите сумму расходов на развлечения: "))

total = food + transport + entertainment
print("Общие расходы: ", total)

average = total / 3
print("Средние расходы: ", average)