import os
import shutil
import platform

project_path = os.path.dirname(os.path.abspath(__file__)) # Корень проекта

def new_folder(folder_name):
    if not os.path.exists(folder_name):
        os.makedirs(folder_name)
        print(f"Папка `{folder_name}` создана")
    else:
        print(f"Папка `{folder_name}` уже существует, всё в порядке!")

def delete_path(name):
    """Удаляет файл или папку в текущей директории."""
    # Определяем путь к текущей директории (где находится этот скрипт)
    full_path = os.path.join(project_path, name)

    if os.path.exists(full_path):
        if os.path.isfile(full_path):  # Если это файл
            os.remove(full_path)
            print(f"Файл '{name}' удалён.")
        elif os.path.isdir(full_path):  # Если это папка
            shutil.rmtree(full_path)
            print(f"Папка '{name}' удалена.")
    else:
        print(f"Объект '{name}' не найден.")

import os
import shutil

def copy_path(src_name, new_name, project_path):
    """Копирует файл или папку в указанной директории с новым именем."""
    src_path = os.path.join(project_path, src_name)  # Путь к исходному объекту
    dst_path = os.path.join(project_path, new_name)  # Новый путь с новым именем

    if os.path.exists(src_path):
        if os.path.isfile(src_path):  # Если файл
            shutil.copy2(src_path, dst_path)
            print(f"Файл '{src_name}' скопирован как '{new_name}'.")
        elif os.path.isdir(src_path):  # Если папка
            shutil.copytree(src_path, dst_path)
            print(f"Папка '{src_name}' скопирована как '{new_name}'.")
    else:
        print(f"Объект '{src_name}' не найден.")

def directory_view(project_path):

    # Получаем список файлов
    files = os.listdir(project_path)

    # Выводим список файлов
    print(f'Список объектов в директории: ', files)


def get_subdirectories(project_path):
    return [name for name in os.listdir(project_path) if os.path.isdir(os.path.join(project_path, name))]

def get_files(project_path):
    return [name for name in os.listdir(project_path) if os.path.isfile(os.path.join(project_path, name))]

def get_system_info():
    info = {
        "ОС": platform.system(),
        "Версия ОС": platform.version(),
        "Имя устройства": platform.node(),
        "Архитектура": platform.architecture()[0],
        "Процессор": platform.processor(),
        "Количество ядер": os.cpu_count(),
    }
    return info

