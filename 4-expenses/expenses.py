""" 9.15 Домашнее задание. Фуннкции. """
expenses: list[str] = []


def get_summ() -> str:
    """ Получение суммы расхода от пользователя """
    return str(input("Введите сумму:")).lower().strip()


def get_format(value: str) -> str | None:
    """ Получение отформатированной суммы расхода """
    temps_summ = value.split()
    is_correect_format: bool = True

    if len(temps_summ) != 2 and len(temps_summ) != 4:
        is_correect_format = False
        print("Некорректный формат суммы")
        return None
    else:
        if len(temps_summ) == 2 and (temps_summ[1] != "руб" or temps_summ[0].isdigit() is False):
            is_correect_format = False
            print("Некорректный формат суммы")
            return None
        elif len(temps_summ) == 4 and (temps_summ[1] != "руб" or temps_summ[3] != "коп" or temps_summ[2].isdigit() is False):
            is_correect_format = False
            print("Некорректный формат суммы")
            return None

    if is_correect_format:
        if len(temps_summ) == 2:
            return f"{temps_summ[0]}.00 ₽"
        else:
            return f"{temps_summ[0]}.{temps_summ[2].zfill(2)} ₽"


def add_expense(expenses: list[str], value: str) -> None:
    """ Добавление расхода в список расходов """
    expenses.append(value)
    print(f"Расход добавлен: {value}")


def delete_expense(expenses: list[str], index: int) -> None:
    """ Удаление расхода по номеру """
    if 0 <= index < len(expenses):
        removed_expense = expenses.pop(index)
        print(f"Расход удалён: {removed_expense}")
    else:
        print("Некорректный номер расхода.")


def get_total(expenses: list[str]) -> float:
    """ Получение общей суммы расходов """
    total: float = 0.0
    for expense in expenses:
        amount_str = expense.replace(" ₽", "")
        total += float(amount_str)
    return total


def get_average(expenses: list[str]) -> float:
    """ Получение среднего расхода """
    if expenses:
        return get_total(expenses) / len(expenses)
    return 0.0


def print_report(expenses: list[str]) -> None:
    """ Печать отчёта о расходах """
    total = get_total(expenses)
    average = get_average(expenses)
    print(f"Общая сумма расходов: {total:.2f} ₽")
    print(f"Средний расход: {average:.2f} ₽")


while True:
    print("1. Добавить расход")
    print("2. Показать все расходы")
    print("3. Показать сумму и средний расход")
    print("4. Удалить расход по номеру")
    print("5. Выход")

    choice: str = input("Выберите действие: ")

    if choice == "1":
        value: str = get_summ()
        formatted_value: str | None = get_format(value)
        if formatted_value is not None:
            add_expense(expenses, formatted_value)
        else:
            print("Расход не добавлен из-за некорректного формата.")
    elif choice == "2":
        if expenses:
            print("Список расходов:")
            for idx, expense in enumerate(expenses):
                print(f"{idx + 1}. {expense}")
        else:
            print("Список расходов пуст.")
    elif choice == "3":
        total = get_total(expenses)
        average = get_average(expenses)
        print(f"Общая сумма расходов: {total:.2f} ₽")
        print(f"Средний расход: {average:.2f} ₽")
    elif choice == "4":
        if expenses:
            print("Список расходов:")
            for idx, expense in enumerate(expenses):
                print(f"{idx + 1}. {expense}")
            delete_expense_choice: str = input(
                "Хотите удалить расход? (да/нет): ").lower()
            if delete_expense_choice == "да":
                try:
                    index_to_delete: int = int(
                        input("Введите номер расхода для удаления: ")) - 1
                    delete_expense(expenses, index_to_delete)
                except ValueError:
                    print("Пожалуйста, введите корректный номер.")
        else:
            print("Список расходов пуст.")
    elif choice == "5":
        print("Выход из программы.")
        break
    else:
        print("Некорректный выбор. Пожалуйста, выберите действие от 1 до 5.")
