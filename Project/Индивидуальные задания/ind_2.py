#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
Прайс-лист компьютерной фирмы включает в себя список моделей продаваемых компьютеров.
Одна позиция списка (Model) содержит марку компьютера, тип процессора, частоту работы процессора,
объем памяти, объем жесткого диска, объем памяти видеокарты, цену компьютера в условных единицах
и количество экземпляров, имеющихся в наличии. Реализовать класс PriceList, полями которого являются
дата его создания, номинал условной единицы в рублях и список продаваемых моделей компьютеров.
В списке не должно быть двух моделей одинаковой марки. В классе PriceList реализовать методы добавления,
изменения и удаления записи о модели, метод поиска информации о модели по марке компьютера, по объему памяти,
диска и видеокарты (равно или не меньше заданного), а также метод подсчета общей суммы. Реализовать методы
объединения и пересечения прайс-листов. Методы добавления и изменения принимают в качестве входного
параметра объект класса Model. Метод поиска возвращает объект класса Model в качестве результата.

Дополнительно к требуемым в заданиях операциям перегрузить операцию индексирования [].
Максимально возможный размер списка задать константой. В отдельном поле size должно храниться
максимальное для данного объекта количество элементов списка; реализовать метод size(), возвращающий
установленную длину. Если количество элементов списка изменяется во время работы,
определить в классе поле count. Первоначальные значения size и count устанавливаются конструктором.

"""


class Model:
    def __init__(self, mark, processor, frequency, memory, hdd, video, price, count):
        self.mark = mark
        self.processor = processor
        self.frequency = int(frequency)
        self.memory = int(memory)
        self.hdd = int(hdd)
        self.video = int(video)
        self.price = float(price)
        self.count = int(count)

    def __repr__(self):
        return f"{self.mark}: {self.processor}/{self.frequency} МГц/{self.memory} Гб/{self.hdd} Гб/{self.video} Мб/{self.price} ус. ед./{self.count} шт.\n"


class PriceList:

    MAX_SIZE = 10

    def __init__(self, date, denomination):
        self.date = date
        self.denomination = denomination
        self.models = []
        self.size = PriceList.MAX_SIZE
        self.count = 0

    def size(self):
        return self.size

    def add_model(self, model):
        if self.count < self.size:
            if model.mark not in self.models:
                self.models.append(model)
                self.count += 1
                print(f"Добавлена модель {model}")
            else:
                print("Данная модель уже находится в списке")

        else:
            print("достигнут максимальный размер списка")

    def remove_model(self, model):
        if model in self.models:
            self.models.remove(model)
            self.count -= 1
            print(f"Модель {model} удалена из списка")

        else:
            print("Данной модели нет в списке")

    def change_model(self, model):
        ch = 0
        for ind, mod in enumerate(self.models):
            if model.mark == mod.mark:
                self.models[ind] = model
                ch = 1
                print("Данные о модели изменены")

        if ch == 0:
            print("Данная модель не найдена в списке")

    def __repr__(self):
        return f"Список {self.date}: {self.denomination} руб./ед: \n{self.models}"

    def find_by_mark(self, mark):
        for model in self.models:
            if model.mark == mark:
                return model
        return None

    def find_by_memory(self, memory):
        for model in self.models:
            if model.memory >= memory:
                return model
        return None

    def find_by_hdd(self, video):
        for model in self.models:
            if model.video >= video:
                return model
        return None

    def sum(self):
        return f"{sum([self.denomination * model.price for model in self.models])} руб."

    def union(self, list_2):
        self.models = list(set(self.models + list_2.models))
        return self

    def intersection(self, list_2):
        self.models = [mod for mod in self.models if mod in list_2.models]
        return self


if __name__ == "__main__":
    list1 = PriceList(date="09-01-24", denomination="1000")
    list1.add_model(
        Model("TREIDCOMPUTERS", "Intel Core i5 4570", 3200, 16, 480, 256, 17.28, 12)
    )
    list1.add_model(
        Model(
            "Raskat Strike 520", "Intel Core i5-10400F", 2900, 16, 1024, 8192, 59.184, 6
        )
    )

    list2 = PriceList(date="11-12-23", denomination="1000")
    list2.add_model(
        Model("TREIDCOMPUTERS", "Intel Core i5 4570", 3200, 16, 480, 256, 17.28, 12)
    )
    list2.add_model(
        Model(
            "ASUS G10DK-A3400G0320",
            "Intel Core i5-12400F",
            2500,
            16,
            1024,
            12288,
            81.216,
            3,
        )
    )

    # Удаление и добавление записи
    list1.remove_model(
        Model(
            "Raskat Strike 520", "Intel Core i5-10400F", 2900, 16, 1024, 8192, 59.184, 6
        )
    )
    list1.add_model(
        Model(
            "Raskat Strike 520", "Intel Core i5-10400F", 2900, 16, 1024, 8192, 59.184, 6
        )
    )

    # Изменение записи
    list2.change_model(
        Model(
            "ASUS G10DK-A3400G0320",
            "AMD Ryzen 5 3400G",
            3700,
            8,
            1024,
            12288,
            58.838,
            4,
        )
    )

    # Вывод содержимого списков
    print("Список 1:")
    print(list1)

    print("\nСписок 2:")
    print(list2)

    # Поиск записи
    find = list1.find_by_mark("TREIDCOMPUTERS")
    print(f"\nНайдена модель: {find}")

    # Операции над списками
    union = list1.union(list2)
    print("\nОбъединение списков:")
    print(union)

    intersection = list1.intersection(list2)
    print("\nПересечение списков:")
    print(intersection)
