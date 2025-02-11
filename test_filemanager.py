from my_bill_t import refill

# Функция для тестирования
def test_refill():
    # Подменяем встроенный input на наш mock-ввод
    original_input = __builtins__.input  # Сохраняем оригинальный input
    __builtins__.input = lambda _: '100'  # Подменяем input на фиксированное значение

    # Тест 1: Проверяем, что функция корректно добавляет сумму пополнения
    result = refill(500)
    assert result == 600, f"Ожидалось 600, получено {result}"

    # Тест 2: Проверяем пополнение на 0
    __builtins__.input = lambda _: '0'  # Подменяем input на 0
    result = refill(500)
    assert result == 500, f"Ожидалось 500, получено {result}"

    # Тест 3: Проверяем отрицательное пополнение
    __builtins__.input = lambda _: '-50'  # Подменяем input на -50
    result = refill(500)
    assert result == 450, f"Ожидалось 450, получено {result}"

    # Возвращаем оригинальный input
    __builtins__.input = original_input

    print("Все тесты прошли успешно!")

# Запуск теста
test_refill()