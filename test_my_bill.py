from my_bill_t import refill

# Подменяем встроенный input
original_input = __builtins__.input
__builtins__.input = lambda _: '100'

# Тестируем функцию refill
result = refill(500)
print(f"Результат: {result}")  # Ожидаемый результат: 600

# Возвращаем оригинальный input
__builtins__.input = original_input