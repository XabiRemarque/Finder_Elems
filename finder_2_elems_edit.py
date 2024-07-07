import sys


# Избыточный комментарий плюс избыточное исключение, IndexError вполне подошел бы
# Определяем собственное исключение для ситуации с некорректной позицией элемента
class RangeError(Exception):
    def __init__(self):
        self.message = "Элемент за пределами списка"

    def __str__(self):
        return self.message


class LenError(Exception):
    def __init__(self):
        self.message = "Пустой список"

    def __str__(self):
        return self.message

# Такие вещи надо выносить в функцию main() удобно по аналогии с другими языками осознавать точку входа в приложение
list_of_nums = []  # Define list_of_nums outside the try block # Коммент на английском? и зачем он?

try:
    # Убери избыточные комментарии и реализуй тестирование в соседнем файле test_problem.py, а в основном файле
    # оставь только функцию
    # Получаем длину списка
    len_of_list = int(input("Введите длину списка: "))

    if len_of_list <= 1:
        raise LenError

    # Получаем позицию элемента
    index = int(input("Введите позицию элемента: "))

    # Проверяем, находится ли позиция элемента в пределах списка
    if index >= len_of_list:
        raise RangeError

    # Получаем элементы списка
    for i in range(len_of_list):
        num = int(input(f"Введите элемент списка {i + 1}: "))
        list_of_nums.append(num)

    # Если позиция в пределах списка, выводим элемент
    print(f"Элемент на позиции {index}: {list_of_nums[index]}")

except RangeError as e:
    print(e)
    sys.exit(1)

except LenError as e:
    print(e)
    sys.exit(1)

except ValueError:
    print("Некорректный ввод. Ожидалось целое число.")
    sys.exit(1)

# В питоне незачем передавать длинну массива, во всех Enumerable коллекциях реализован метод __len__()
# Я не помню о чем задача и из именования мне совсем не легче, если это задача на K ближайших элементов, то причем тут 2?
def find_2_elements(ind: int, len_of_lst: int, lst: list) -> list:
    if len_of_lst <= 2:
        del lst[ind]
        return lst

    abs_lst = [abs(lst[i] - lst[ind]) for i in range(len(lst))]
    min_el_r = min(abs_lst[ind + 1 :])
    c_r = abs_lst[ind + 1 :].count(min_el_r) + 1
    min_el_l = min(abs_lst[:ind])
    c_l = abs_lst[:ind].count(min_el_l) + 1

    if ind + 1 == len_of_lst:
        num = lst.count(lst[1])
        return sorted([lst[ind - 1], lst[ind - num]])

    if ind == 0:
        num = lst.count(lst[1])
        return sorted([lst[1], lst[1 + num]])

    if min_el_l == min_el_r:
        return sorted([lst[ind - 1], lst[ind + 1]])

    elif min_el_l < min_el_r:
        if len(lst[: ind - c_r]) == 0 and not (abs_lst[ind - c_l] < min_el_r):
            return sorted([lst[ind - 1], lst[ind + 1]])
        elif abs_lst[ind - c_l] < min_el_r:
            return sorted([lst[ind - c_l], lst[ind - 1]])

    else:
        if len(lst[ind + c_l :]) == 0 and not (abs_lst[ind + c_r] < min_el_l):
            return sorted([lst[ind + 1], lst[ind - 1]])
        elif abs_lst[ind + c_r] < min_el_l:
            return sorted([lst[ind + c_r], lst[ind + 1]])


print(f"Исходный массив: {' '.join([str(i) for i in list_of_nums])}")
elem = list_of_nums[index]
print(f"Искомое число: {elem}, его индекс: {index}")

output_list = find_2_elements(index, len_of_list, list_of_nums)
for i, v in enumerate(output_list, 1):
    print(f"{i}-й элемент равен {v}")
