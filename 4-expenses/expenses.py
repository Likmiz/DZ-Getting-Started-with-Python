# summ: str = str(input("Введите сумму:")).lower().strip()

# temps_summ = summ.split()
# is_correect_format: bool = True

# if len(temps_summ) != 2 and len(temps_summ) != 4:
#     is_correect_format = False
#     print("Некорректный формат суммы")
# else:
#     if len(temps_summ) == 2 and (temps_summ[1] != "руб" or temps_summ[0].isdigit() == False):
#         is_correect_format = False
#         print("Некорректный формат суммы")
#     elif len(temps_summ) == 4 and (temps_summ[1] != "руб" or temps_summ[3] != "коп" or temps_summ[2].isdigit() == False):
#         is_correect_format = False
#         print("Некорректный формат суммы")

# if is_correect_format:

#     if len(temps_summ) == 2:
#         print(f"{temps_summ[0]}.00 ₽")
#     else:
#         print(f"{temps_summ[0]}.{temps_summ[2].zfill(2)} ₽")

expenses: list = []  # type: ignore
while True:
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать сумму и средний расход")
    print("4. Удалить расход по номеру")
    print("5. Выход")

    choice: str = input("Выберите действие: ")

    if choice == "5":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите 1, 2 или 3.")
