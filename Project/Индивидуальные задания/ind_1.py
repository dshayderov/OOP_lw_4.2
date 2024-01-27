#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Поле first — дробное число; поле second — целое число, показатель степени.
Реализовать метод power() — возведение числа first в степень second.
Метод должен правильно работать при любых допустимых значениях first и second.
"""


class Exp:
    def __init__(self, a=0, b=0):
        a = float(a)
        b = int(b)

        self.__first = a
        self.__second = b

    # Клонировать выражение.
    def __clone__(self):
        return Exp(self.__first, self.__second)

    @property
    def first(self):
        return self.__first

    @first.setter
    def first(self, value):
        self.__first = float(value)

    @property
    def second(self):
        return self.__second

    @second.setter
    def second(self, value):
        self.__second = int(value)

    # Привести выражение к строке.
    def __str__(self):
        return f"{self.__first} ^ {self.__second}"

    def __repr__(self):
        return self.__str__()

    # Возведение в степень
    def __ipow__(self):
        return self.__first ** self.__second

    def __pow__(self):
        return self.clone().__ipow__()


if __name__ == "__main__":
    exm1 = Exp(4.5, 2)
    print(f"exm1 = {exm1}")

    exm2 = exm1.__pow__()
    print(f"exm2 = {exm2}")
