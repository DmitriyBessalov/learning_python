# https://pythonworld.ru/osnovy/tasks.html


import time


def s_year_leap(year):
    """Задача 2"""
    if year % 2:
        return 'false'
    else:
        return 'true'


def bank(a, years):
    """Задача 5"""
    i = 0
    while i < years:
        a = round(a * 1.1, 2)
        i += 1
    return a


def date(dd, mm, yyyy):
    """Задача 7"""
    try:
        time.strptime(str(dd) + '.' + str(mm) + '.' + str(yyyy), '%d.%m.%Y')
        return 'Дата существует'
    except ValueError:
        return 'Дата несуществует'