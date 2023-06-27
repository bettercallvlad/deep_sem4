# Задание №4
# Функция получает на вход список чисел.
# Отсортируйте его элементы in place без использования встроенных
# в язык сортировок.
# Как вариант напишите сортировку пузырьком. Её описание есть в википедии.


def bubble_sort(nums: list[int]) -> list[int]:
    """Сортировка пузырьком"""

    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            if nums[i] < nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
    return nums


num_list = [1, 3, 2, 5]
bubble_sort(num_list)

print(num_list)
