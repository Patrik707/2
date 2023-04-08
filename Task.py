# 1
'''
Задача: Написать программу, которая из имеющегося массива строк формирует новый массив из строк,
длина которых меньше, либо равна 3 символам.
Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма.
При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.
'''


def filter_names(names, lenght_filter = 3):
    result = []

    for name in names:
        if len(name) <= lenght_filter:
            result.append(name)

    return result


names = ['Robert', 'Tom', 'Sonia', 'Sherri', 'Rob', 'Jackie', 'Chris', 'Kat']
result = filter_names(names)

print(f'Original list:\n'
      f'{names}.\n\n'
      f'Filtered list:\n'
      f'{result}.')
