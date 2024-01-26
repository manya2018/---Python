
# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Bottle:
    def __init__(self, capacity_volume: float, occupied_volume: float):
        """
        Создание и подготовка к работе объекта "Бутылка"

        :param capacity_volume: Объем Бутылки
        :param occupied_volume: Объем занимаемой жидкости

        Примеры:
        >>> glass = Bottle(400, 350)  # инициализация экземпляра класса
        """
        if not isinstance(capacity_volume, (int, float)):
            raise TypeError("Объем бутылки должен быть типа int или float")
        if capacity_volume <= 0:
            raise ValueError("Объем бутылки должен быть положительным числом")
        self.capacity_volume = capacity_volume

        if not isinstance(occupied_volume, (int, float)):
            raise TypeError("Количество жидкости должно быть int или float")
        if occupied_volume < 0:
            raise ValueError("Количество жидкости не может быть отрицательным числом")
        self.occupied_volume = occupied_volume

    def is_empty_bottle(self) -> bool:
        """
        Функция которая проверяет является ли бутылка пустой

        :return: Является ли бутылка пустой

        Примеры:
        >>> glass = Bottle(400, 350)
        >>> glass.is_empty_bottle()
        """
        ...

    def add_water_to_bottle(self, water: float) -> None:
        """
        Добавление воды в бутылку.
        :param water: Объем добавляемой жидкости

        :raise ValueError: Если количество добавляемой жидкости превышает свободное место в бутылке, то вызываем ошибку

        Примеры:
        >>> glass = Bottle(400, 350)
        >>> glass.add_water_to_bottle(200)
        """
        if not isinstance(water, (int, float)):
            raise TypeError("Добавляемая жидкость должна быть типа int или float")
        if water < 0:
            raise ValueError("Добавляемая жидкость должна положительным числом")
        ...

    def remove_water_from_bottle(self, estimate_water: float) -> None:
        """
        Извлечение воды из бутылки.

        :param estimate_water: Объем извлекаемой жидкости
        :raise ValueError: Если количество извлекаемой жидкости превышает количество воды в бутылке,
        то возвращается ошибка.

        :return: Объем реально извлеченной жидкости

        Примеры:
        >>> glass = Bottle(500, 500)
        >>> glass.remove_water_from_bottle(200)
        """
        if estimate_water > self.occupied_volume:
            raise ValueError("Количетсво извлекаемой жидкости превышает количестов имеющейся")
        ...


if __name__ == "main":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass

class Animal:
    def __init__(self, species: str, age: str):
        """
        Создание объекта "Животное"

        :param species: Вид животного
        :param age: Возраст животного

        Примеры:
        >>> cat = Animal("Cat", 10)  # инициализация экземпляра класса
        """
        if not isinstance(species,str):
            raise TypeError("Тип животного должен быть типа str ")
        self.species = species
        if not isinstance(age,(int, float)):
            raise TypeError("Возраст животного должен быть типа int или float ")
        self.age = age

    def add_offspring(self, children: int) -> None:
        """
        Добавление потомства животному.

        :param children: Количество детенышей

        Примеры:
        >>> cat = Animal("Cat", 10)
        >>> cat.add_offspring(3)
        """
        if not isinstance(children, (int, float)):
            raise TypeError("Количество детенышей должно быть типа int или float")
        if children <= 0:
            raise ValueError("Количетсво детей должно быть положительным числом")
        self.children = children
        ...

    def add_owner(self,owner: str) -> None:
        """
        Добавить хозяина животному.

        : param owner: Имя хозяина животного
        Примеры:
        >>> cat = Animal("Cat", 10)
        >>> cat.add_owner("Maria")
        """
        if not isinstance(owner,str):
            raise TypeError("Имя хозяина долдно быть типа str")

        ...

#
class ElectronicDevice:
    def __init__(self, brand: str, model: str):
        """
        Создание объекта "Электронное устройство"

        :param brand: Бренд устройства
        :param model: Модель устройства

        Примеры:
        >>> phone = ElectronicDevice("Apple", "iPhone")  # инициализация экземпляра класса
        """
        if not isinstance(brand, str ):
            raise TypeError("Бренд устройства должен быть str")
        self.brand = brand
        if not isinstance(brand, str ):
            raise TypeError("Модель устройства должена быть str")
        self.model = model
    def add_owner(self,owner: str) -> None:
        """
        Добавить владельца устройству.

        : param owner: Имя владельца устройста
        >>> phone = ElectronicDevice("Apple", "iPhone")
        >>> phone.add_owner("Maria")
        """
        if not isinstance(owner,str):
            raise TypeError("Имя владельца должно быть типа str")

    def add_color(self,color) -> None:
        """
        Добавление цвета устройста.
        : param color: Цвет устройста
        Примеры:
        >>> phone = ElectronicDevice("Apple", "iPhone")
        >>> phone.add_color("red")
        """
        if not isinstance(color,str):
            raise TypeError("Цвет устройста должен быть типа str")
        ...


if __name__ == "main":
    doctest.testmod()  # тестирование примеров, которые находятся в документации
    pass