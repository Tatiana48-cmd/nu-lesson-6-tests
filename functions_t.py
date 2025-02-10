"""
    Программа Python для фильтрации нечетных чисел
    в списке, используя функцию filter()
"""

# список чисел
numbers = [1, 2, 4, 5, 7, 8, 10, 11]

# функция, которая проверяет числа
def filter_odd_num(in_num):
    if(in_num % 2) == 0:
        return True
    else:
        return False

# Применение filter() для удаления нечетных чисел
out_filter = filter(filter_odd_num, numbers)

def plus(numbers):
  return sum(numbers)

x = map(plus, [numbers])

# Сортируем список
numbers_sort = sorted(numbers, reverse=True)



if __name__ == '__main__':

    print("Тип объекта out_filter: ", type(out_filter))
    print("Отфильтрованный список: ", list(out_filter))
    print(sum(numbers))
    print(list(x))
    print('Отсортированный список:')
    print(numbers_sort)


