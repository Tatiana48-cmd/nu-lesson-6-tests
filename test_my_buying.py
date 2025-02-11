from my_bill_t import buying


# Исходная функция
def buying(balance, history):
    sum_buying = int(input('Введите сумму покупки: '))
    if sum_buying <= balance:
        name_buying = input('Введите название покупки: ')
        balance -= sum_buying
        history.append((name_buying, sum_buying))
        print(f'Покупка {name_buying} на сумму {sum_buying} рублей совершена.')
    else:
        print('Недостаточно средств!')
    return balance


# Тест
def test_buying():
    # Подготовка данных
    balance = 1000  # Начальный баланс
    history = []    # Пустая история покупок

    # Сохраняем оригинальный input
    original_input = __builtins__.input

    # Тест 1: Успешная покупка
    print("\nТест 1: Успешная покупка")

    # Подменяем input для суммы покупки и названия
    def mock_input(prompt):
        if "сумму" in prompt:
            return '500'  # Сумма покупки
        elif "название" in prompt:
            return 'Тестовая покупка'  # Название покупки
        else:
            return ''  # На случай других запросов

    __builtins__.input = mock_input

    # Выполняем покупку
    new_balance = buying(balance, history)

    # Проверяем результаты
    assert new_balance == 500, f"Ожидалось 500, получено {new_balance}"
    assert history == [("Тестовая покупка", 500)], f"История не совпадает: {history}"

    # Тест 2: Недостаточно средств
    print("\nТест 2: Недостаточно средств")
    balance = 100  # Уменьшаем баланс

    # Подменяем input для суммы покупки
    __builtins__.input = lambda _: '600'  # Сумма покупки

    # Выполняем покупку
    new_balance = buying(balance, history)

    # Проверяем результаты
    assert new_balance == 100, f"Ожидалось 100, получено {new_balance}"
    assert len(history) == 1, f"История не должна изменяться: {history}"

    # Возвращаем оригинальный input
    __builtins__.input = original_input

    print("\nВсе тесты прошли успешно!")


# Запуск теста
test_buying()