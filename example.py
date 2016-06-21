# -*- coding: utf-8 -*-
"""
Задание: Суть в том, чтоб отрефакторить данный пример (а лучше начать своё сначала) таким образом, чтоб
в конечном итоге у вас был объект House со всем внутренностями.
Сейчас есть видимая проблема с этим кодом (помимо того, что он не делиет ничего полезного и не работает) -
указание координат комнаты для дома, и координат мебели для комнаты
И если хватит времени - подготовить почву для экспорта-импорта этих объектов (или объекта. я ещё не решил)
"""
from abc import ABCMeta, abstractmethod


class VolumeMixin(object):
    """
    mixin, который предоставляет свойство {size},
    и рассчитывает его на основе полей класса
    (тут я имею ввиду вн. объём)
    """

    @property
    def volume(self):
        """
        тут мы можем делегировать вызов к self.get_volume()
        для расчёта размера, например House может реализовать это как сумму всех комнат + чердак, если есть
        или просто переопределить это свойство в наследниках
        """
        return self.get_volume()

    def get_volume(self):
        """
        Так делать необязательно, но может оказаться полезным,
        если мы хотим иметь больше контроля над свойством в будущем
        """
        pass


class WeightMixin(object):
    pass


class Furniture(WeightMixin, object):
    """
    объект мебели, в зависимости от требуемого уровня детализации - можно ввести подклассы для каждого типа мебели
    можно домешать сюда Volume и предоставить объём, если мы планируем его использовать
    ---
    Я подмешал сюда WeightMixin, чтоб показать, что у каждого типа мебели будет вес
    """
    material = None

    def __init__(self, material):
        self.material = material


class Table(Furniture):
    """
    Стол имеет какую-то особенность
    """
    pass


class Chair(Furniture):
    pass


class Refrigerator(Furniture):
    """
    Для классов такого типа можно создать ещё один подтип, например Appliance, и наследовать всё от него
    """
    pass


class Room(VolumeMixin, object):
    """
    базовый класс для всех комнат
    Решение о том, где хранить координаты мебели и дверей/окон остаются за вами
    Вы можете создать ещё один слой, например ObjectsWithLocation,
    который будет хранить объект, его родителя и координаты, но выбор за вами
    """
    furniture = None
    # Тут под окнам могут подразумеваться так-же двери
    windows = []

    def __init__(self, furniture):
        self.furniture = furniture

    @property
    def volume(self):
        pass


class Kitchen(Room):
    """
    Тоже какие-то особые свойства
    """
    pass


class Bedroom(Room):
    pass



class House(WeightMixin, VolumeMixin, object):
    rooms = None
    # Какие-то дополнительные свойства
    properties = None

    def __init__(self, rooms, properties):
        self.rooms = rooms
        self.properties = properties

    @property
    def volume(self):
        """
        Сейчас объём дома == объёму всех комнат входящих в него
        т.е. мы не учитываем ещё многих вещей
        """
        return sum([room.volume for room in self.rooms])


house = House([
    Kitchen([
        Refrigerator(),
    ]),
    Bedroom([
        Chair(),
        Table(),
    ]),
])


class Encoder(object):
    __metaclass__ = ABCMeta

    @abstractmethod
    def load(self, data):
        """
        Загружает данные из строки и возвращает сконструированный объект
        :param data:
        :return: Получившийся объект
        """
        pass

    @abstractmethod
    def dump(self, obj):
        """
        ПОлучив объект - возвращает строку в каком-либо формате
        :param obj:
        :return:
        """
        pass


class JSONEncoder(Encoder):
    pass


class YAMLEncoder(Encoder):
    """
    Тоже самое, только используя yaml
    """
    pass

