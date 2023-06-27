# Задание №2
# Напишите функцию, которая принимает строку текста.
# Сформируйте список с уникальными кодами Unicode каждого
# символа введённой строки отсортированный по убыванию.


def get_unicode_list(text: str) -> list[int]:
    """принимает строку текста. Возвращает список с уникальными
    кодами Unicode каждого символа введённой строки
    отсортированный по убыванию. """
    return sorted(list(map(ord, text)), reverse=True)


print(get_unicode_list('функцию'))
