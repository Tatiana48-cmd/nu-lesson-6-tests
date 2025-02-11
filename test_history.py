from io import StringIO
import sys
from my_bill_t import show_history


def capture_output(func, *args, **kwargs):
    old_stdout = sys.stdout
    sys.stdout = StringIO()
    try:
        func(*args, **kwargs)
        return sys.stdout.getvalue()
    finally:
        sys.stdout = old_stdout


def test_show_history():
    history = [("Молоко", 100), ("Хлеб", 50), ("Яблоки", 150)]
    output = capture_output(show_history, history)
    expected_output = "История покупок:\nМолоко: 100 рублей\nХлеб: 50 рублей\nЯблоки: 150 рублей\n"
    assert output == expected_output, f"Ожидалось: {expected_output}, получено: {output}"

    history = []
    output = capture_output(show_history, history)
    expected_output = "История покупок пуста.\n"
    assert output == expected_output, f"Ожидалось: {expected_output}, получено: {output}"

print('Проверка прошла успешно')
test_show_history()
