#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def multiply_until_zero():
    """
    Считывает числа с клавиатуры и перемножает их до ввода 0.
    Возвращает полученное произведение.
    """
    product = 1
    while True:
        num = float(input("Введите число (для завершения введите 0): "))
        if num == 0:
            break
        product *= num
    return product


def main():
    """
    Главная функция программы.
    """
    result = multiply_until_zero()
    print(f"Произведение введенных чисел: {result}")


if __name__ == '__main__':
    main()
