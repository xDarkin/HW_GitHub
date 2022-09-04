
"""Модуль для підключення функцій сортування списків."""


def sort_bubble(*args: list):
    """
    :param args: отримує на вхід список
    :return: повертає відсортований список
    """
    """Функція сортування методом бульбашки. Приймає на вхід список та сортує його.
        Порівнює сусідні елементи та міняє їх місцями."""
    args = list(*args)
    n = len(args)
    for i in range(n-1):
        for j in range(n-2, i-1, -1):
            if args[j+1] < args[j]:
                args[j], args[j+1] = args[j+1], args[j]
    return args


def sort_choice(*args: list):
    """
    :param args: отримує на вхід список
    :return: повертає відсортований список
    """
    """Функція сортування методом вибору. Приймає на вхід список та сортує його.
        Послідовно порівнює один елемент з іншими, доки не знайде менший, та міняє їх місцями."""
    args = list(*args)
    n = len(args)
    for i in range(n-1):
        n_min = i
        for j in range(i+1, n):
            if args[j] < args[n_min]:
                n_min = j
        if i != n_min:
            args[i], args[n_min] = args[n_min], args[i]
    return args


def partition(lst, low, high):
    pivot = lst[(low + high) // 2]
    i = low - 1
    j = high + 1
    while True:
        i += 1
        while lst[i] < pivot:
            i += 1
        j -= 1
        while lst[j] > pivot:
            j -= 1
        if i >= j:
            return j
        lst[i], lst[j] = lst[j], lst[i]


def sort_quick(lst: list):
    """
    :param lst: отримує на вхід список
    :return: повертає відсортований список
    """
    """Функція сортування методом швидкого сортування. Приймає на вхід список та сортує його.
        Міняє місцями елемени більші та менші ніж центральний елемент,
        поступово признааючи нові центральні елементи для кожної попередньо відсортованої половини списку."""
    def _sort_quick(lst_m, low, high):
        if low < high:
            split_index = partition(lst, low, high)
            _sort_quick(lst_m, low, split_index)
            _sort_quick(lst_m, split_index+1, high)
    _sort_quick(lst, 0, len(lst)-1)
    return lst


__all__ = ["sort_bubble", "sort_choice", "sort_quick"]


if __name__ == "__main__":
    lst_1 = [21, 33, 5, 87, 9, 12, 57, 37]
    lst_2 = [12, 99, 35, 47, 21, 68, 6]
    lst_3 = [99, 35, 23, 59, 84, 5, 12, 49, 47]
    print(lst_1)
    print(lst_2)
    print(lst_3)
    lst_1 = sort_bubble(lst_1)
    lst_2 = sort_choice(lst_2)
    lst_3 = sort_quick(lst_3)
    print(lst_1)
    print(lst_2)
    print(lst_3)
