""" Пример замыканий - функция присваивается переменной и не удаляется мусорщиком"""


def counter():
    count = 0

    def ended():
        nonlocal count
        count += 1
        return count

    return ended


counter1 = counter()
print(counter1())
# print(counter1())
# print(counter1())
# print(counter1())
# print(counter1())
# print(counter1())
# print(counter1())

"""Пример декораторов """
#
#
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         title = func(*args, **kwargs)
#         print(args)
#         if "end" in kwargs:
#             title += kwargs["end"]
#         return title
#
#     return wrapper
#
#
# @decorator
# def fn(s, end="."):
#     return s
#
#
# print(fn("hi there", end="!!!"))

########################################################################################################################

import time
#
# """Замедление выполнения функции:"""
# def decorator(func):
#     def wrapper(*args, **kwargs):
#         title = func(*args, **kwargs)
#         print(type(args[0]))
#         if not args[1]:
#             print(args[0])
#         else:
#             time.sleep(args[1])
#             print(f"После задержки в {args[1]} секнуд, было напечатано {args[0]}")
#         return title
#     return wrapper
#
#
# @decorator
# def fn(s, slowed):
#     return s, slowed
#
#
# fn("Тестовый текст", 0)

import random
import datetime


# def decorator(func):
#     def wrapper(*args, **kwargs):
#         time1 = time.time()
#         func()
#         print(round(time.time() - time1, 2))
#
#     return wrapper
#
#
# @decorator
# def sleep_function(upper_line=1000):
#     rnd = random.randint(0, upper_line)
#     time.sleep(rnd / 100)
#
#
# sleep_function()

# def decorator(func):
#     cache = {}
#
#     def wrapper(*args, **kwargs):
#         key = func(*args, **kwargs)
#         print(cache)
#         if key in cache:
#             print(f"Используется кэш {cache[key]}")
#             return cache[key]
#         else:
#             result = func(*args, **kwargs)
#             cache[key] = result
#             return result
#
#     return wrapper
#
#
# @decorator
# def multiply(a, b):
#     return a * b




