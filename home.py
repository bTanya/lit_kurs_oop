
from abc import ABCMeta, abstractmethod


class VolumeMixin(object):
    """
    mixin, который предоставляет свойство {size},
    и рассчитывает его на основе полей класса
    (тут я имею ввиду вн. объём)
    """
    def __init__(self, x, y, width, length, height):
        self.x = x
        self.y = y
        self.width = width
        self.length = length
        self.height = height
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

from math import sqrt
class Furniture(object,):

    material = None
    color = None

    def __init__(self,VolumeMixin, material,color):
        self.material = material

        self.color = color
    def distanceObject(self,furniture):
        return sqrt((VolumeMixin.x - (furniture.x+furniture.width) ** 2) + ((VolumeMixin.y - furniture.y) ** 2))


class Table(Furniture):
    def __init__(self, VolumeMixin,  heightTableTop, widthTableTop):
        super(Furniture).__init__(VolumeMixin )
        self.heightTableTop = heightTableTop
        self.widthTableTop = widthTableTop
    def areaTableTop(self):
        return self.heightTableTop * self.widthTableTop
    pass

class Bed(Furniture):
    def __init__(self,VolumeMixin, access):
        super(Furniture).__init__ (VolumeMixin)
        def make(self):
            self.access = True
        def use(self):
            self.access = False


class Technics(Furniture):
    def __init__(self, VolumeMixin,  kwPerHour):
        super(Furniture).__init__(VolumeMixin)
        self.kwPerHour = kwPerHour
        self.turnedOn = False

    def turn_on(self):
        self.turnedOn = True

    def turn_off(self):
        self.turnedOn = False

class Refrigerator(Technics):
    modesTemperature = ['0..+3', '+3..+10', '+10..+20', '-5..0']
    curMode = '0..+3'
    def turn_on(self, mode):
        if mode in self.modesTemperature:
            curMode = mode
    pass

class WashingMachine(Technics):
    def __init__(self, VolumeMixin, kwPerHour,weightLimit):
        super(Technics).__init__(VolumeMixin,kwPerHour)
    clothes_weight = 0
    modes = ['wool', 'cotton', 'daily quick', 'synthetics']
    cur_mode = 'daily_quick'
    def load(self, clothesWeight):
        self.clothesWeight = clothesWeight
        if clothesWeight > self.weightLimit:
            print ("ERR weightLimit")
    def turn_on(self, mode):
        if mode in self.modes:
            cur_mode = mode

class Entrance:
    def __init__(self, VolumeMixin, is_window, is_open=False):
        self.is_window = is_window
        self.is_open = is_open
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

    def __init__(self, VolumeMixin,furniture,Entrance):
        self.furniture = furniture

    def
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