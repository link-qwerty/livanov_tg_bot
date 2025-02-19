# Imports
from datetime import datetime

# Defines
def time_of_day_hello():
    """
    Приветствие с указанием времени суток

    Утилитарная функция для составления фонетически правильного приветствия, содержащего время суток. Возвращает
    нелокализованную строку (ru) с приветствием, соответствующему времени суток
    :return: Строка приветствия
    """

    hour = int(datetime.now().strftime('%H'))
    timedict = {'Доброй ночи': range(0, 5),
                'Доброе утро': range(6, 11),
                'Добрый день': range(12, 16),
                'Добрый вечер': range(17, 23)}

    for key, value in timedict.items():
        if hour in value:
           return key

def time_of_day():
    """
    Время суток

    Утилитарная функция для определения времени суток. Возвращает нелокализованную строку (ru) с временем суток
    :return: Строка представления времени суток
    """

    hour = int(datetime.now().strftime('%H'))
    timedict = {'ночь': range(0, 5),
                'утро': range(6, 11),
                'день': range(12, 16),
                'вечер': range(17, 23)}

    for key, value in timedict.items():
        if hour in value:
           return f'{datetime.now().strftime('%H:%M')}, {key}'