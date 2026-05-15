summ: str = str(input("Введите сумму:")).lower().strip()

temps_summ = summ.split()
is_correect_format: bool = True

if len(temps_summ) != 2 and len(temps_summ) != 4:
    is_correect_format = False
    print("Некорректный формат суммы")
else:
    if len(temps_summ) == 2 and (temps_summ[1] != "руб" or temps_summ[0].isdigit() == False):
        is_correect_format = False
        print("Некорректный формат суммы")
    elif len(temps_summ) == 4 and (temps_summ[1] != "руб" or temps_summ[3] != "коп" or temps_summ[2].isdigit() == False):
        is_correect_format = False
        print("Некорректный формат суммы")

if is_correect_format:

    if len(temps_summ) == 2:
        print(f"{temps_summ[0]}.00 ₽")
    else:
        print(f"{temps_summ[0]}.{temps_summ[2].zfill(2)} ₽")
