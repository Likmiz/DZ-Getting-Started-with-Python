price = float(input("Введите цену товара: "))
discount = float(input("Введите размер скидки в процентах: "))

total_discount = price * (discount / 100)
final_price = price - total_discount

print("Сумма скидки: ", total_discount)
print("Финальная цена: ", final_price)