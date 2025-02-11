import os
import shutil
import tempfile
from my_functions_t import copy_path

import os
import shutil
import tempfile

def test_copy_path():
    # Создаем временную директорию для тестов
    with tempfile.TemporaryDirectory() as temp_dir:
        # Переходим во временную директорию
        os.chdir(temp_dir)

        # Создаем тестовый файл
        test_file = "test_file.txt"
        with open(test_file, "w") as f:
            f.write("Тестовое содержимое файла.")

        # Создаем тестовую папку
        test_dir = "test_dir"
        os.makedirs(test_dir)

        # Тест 1: Копирование файла
        new_file = "new_file.txt"
        copy_path(test_file, new_file, temp_dir)
        assert os.path.exists(os.path.join(temp_dir, new_file)), f"Файл '{new_file}' не был создан."
        print("Тест 1: Копирование файла прошло успешно.")

        # Тест 2: Копирование папки
        new_dir = "new_dir"
        copy_path(test_dir, new_dir, temp_dir)
        assert os.path.exists(os.path.join(temp_dir, new_dir)), f"Папка '{new_dir}' не была создана."
        print("Тест 2: Копирование папки прошло успешно.")

        # Тест 3: Попытка копирования несуществующего объекта
        non_existent = "non_existent.txt"
        copy_path(non_existent, "new_name.txt", temp_dir)
        assert not os.path.exists(os.path.join(temp_dir, "new_name.txt")), "Несуществующий объект был скопирован."
        print("Тест 3: Обработка несуществующего объекта прошла успешно.")

        print("\nВсе тесты прошли успешно!")

# Запуск теста
test_copy_path()