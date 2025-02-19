# Imports
import json

# Defines
class JSONHandler:
    """
    Класс-обработчик данных

    Объекты класса хранят данные, загруженные из файлов JSON и отдают их по запросу

    Методы
    ----------------
        __init__(self, filename: str)
            Конструктор: Инициализация
        parse(self, intent: str)
            Парсинг данных
    Атрибуты
    ----------------
        :cvar {any} __instance: Экземпляр класса (синглетон)
        :ivar {str} filename: Имя файла JSON
        :ivar {any} __data__: Данные JSON
    """

    __instance = None

    def __new__(cls, *args, **kwargs):
        """

        :param args:
        :param kwargs:
        """

        if cls.__instance is None:
            cls.__instance = super().__new__(cls)
        return cls.__instance

    def __init__(self, filename: str):
        """
        Конструктор: Инициализация

        Создает объект-хэндлер для загрузки и парсинга JSON-файлов
        :param str filename: Имя файла JSON
        """

        self.__filename = filename
        with open(self.__filename, 'r', encoding= 'utf-8') as file:
            self.__data = json.load(file)

    def parse(self, section: str, key: str):
        """
        Парсинг данных

        Возвращает данные из JSON по секции и ключу в ней. Если задан аргумент morph, то производится подстановка
        значений
        :param section: Секция данных (словарь)
        :param key: Ключ секции (ключ словаря)
        :return: Содержимое ключа
        """

        return self.__data[section][key]
