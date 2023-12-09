# TODO Написать 3 класса с документацией и аннотацией типов
import doctest


class Table:
    def __init__(self, length: float, width: float, height: float, material: str):
        """
        Создание и подготовка к работе объекта "Стол"

        :param length: Длина стола
        :param width: Ширина стола
        :param height: Высота стола
        :param material: Материал, из которого сделан стол

        :list items: Набор предметов, которые стоят на столе

        Примеры:
        >>> table = Table(1, 1, 1, "Дуб") # инициализация объекта класса "Table"
        """
        if not isinstance(length, (int, float)):
            raise TypeError("Длина стола должна быть числом")
        if length <= 0:
            raise ValueError("Длина стола должна быть положительным числом")
        self.length = length

        if not isinstance(width, (int, float)):
            raise TypeError("Ширина стола должна быть числом")
        if width <= 0:
            raise ValueError("Ширина стола должна быть положительным числом")
        self.width = width

        if not isinstance(height, (int, float)):
            raise TypeError("Высота стола должна быть числом")
        if height <= 0:
            raise ValueError("Высота стола должна быть положительным числом")
        self.height = height

        if not isinstance(material, str):
            raise TypeError("Материал должен быть строкой")
        if material == "":
            raise ValueError("Материал не может быть пустой строкой")

        self.items = []

    def add_item(self, item: str) -> None:
        """
        Добавляет предмет на стол
        :param item: Название предмета, помещаемого на стол

        Примеры:
        >>> table = Table(1, 1, 1, "Пластик")
        >>> table.add_item("Кружка")
        """
        if not isinstance(item, str):
            raise TypeError("Предмет должен быть строкой")
        if item == "":
            raise ValueError("Предмет не может быть пустой строкой")
        ...

    def search_item(self, item: str) -> bool:
        """
        Проверяет, есть ли предмет на столе
        :param item: Название предмета, который нужно найти

        :return: Находится ли предмет на столе

        Примеры:
        >>> table = Table(1, 1, 1, "Пластик")
        >>> table.add_item("Кружка")
        >>> table.search_item("Кружка") # True
        """
        ...


class Button:
    def __init__(self, x: int, y: int):
        """
        Создание и подготовка в работе класса "Кнопка"
        :param x: Координата по оси x
        :param y: Координата по оси y

        Примеры:
        >>> button = Button(0, 0) # инициализация объекта класса Button
        """
        if not isinstance(x, int):
            raise TypeError("Координата x должна быть целым числом")
        self.x = x
        if not isinstance(y, int):
            raise TypeError("Координата y должна быть целым числом")
        self.y = y
        self.is_pressed = False

    def switch(self) -> bool:
        """
        Переключает кнопку

        :return: Возвращает новое состояние кнопки
        Примеры:
        >>> button = Button(0, 0)
        >>> button.switch()
        """
        ...

    def change_position(self, x: int, y: int) -> None:
        """
        Меняет положение кнопки
        :param x: Координата по оси x
        :param y: Координата по оси y

        Примеры:
        >>> button = Button(0, 0)
        >>> button.change_position(128, 128)
        """
        if not isinstance(x, int):
            raise TypeError("Координата x должна быть целым числом")
        if not isinstance(y, int):
            raise TypeError("Координата y должна быть целым числом")
        ...


class Brush:
    def __init__(self, red: int, green: int, blue: int, width: int):
        """
        Создание и подготовка к работе класса "Кисть"

        :param red: Красная составляющая цвета кисти
        :param green: Зелёная составляющая цвета кисти
        :param blue: Синяя составляющая цвета кисти
        :param width: Толщина кисти

        Пример:
        >>> brush = Brush(255, 255, 255, 2)
        """
        if not isinstance(red, int):
            raise TypeError("Красный цвет должен задаваться целым числом")
        if red < 0 or red > 255:
            raise ValueError("Красный цвет должен задаваться неотрицательным числом меньше 256")
        self.red = red
        if not isinstance(green, int):
            raise TypeError("Зелёный цвет должен задаваться целым числом")
        if green < 0 or green > 255:
            raise ValueError("Зелёный цвет должен задаваться неотрицательным числом меньше 256")
        self.green = green
        if not isinstance(blue, int):
            raise TypeError("Синий цвет должен задаваться целым числом")
        if blue < 0 or blue > 255:
            raise ValueError("Синий цвет должен задаваться неотрицательным числом меньше 256")
        self.blue = blue
        if not isinstance(width, int):
            raise TypeError("Толщина кисти должна задаваться целым числом")
        self.width = width

    def change_color(self, red: int, green: int, blue: int) -> None:
        """
        Меняет цвет кисти

        :param red: Красная составляющая цвета кисти
        :param green: Зелёная составляющая цвета кисти
        :param blue: Синяя составляющая цвета кисти

        Пример:
        >>> brush = Brush(0, 0, 0, 2)
        >>> brush.change_color(255, 0, 0)
        """
        if not isinstance(red, int):
            raise TypeError("Красный цвет должен задаваться целым числом")
        if red < 0 or red > 255:
            raise ValueError("Красный цвет должен задаваться неотрицательным числом меньше 256")
        self.red = red
        if not isinstance(green, int):
            raise TypeError("Зелёный цвет должен задаваться целым числом")
        if green < 0 or green > 255:
            raise ValueError("Зелёный цвет должен задаваться неотрицательным числом меньше 256")
        self.green = green
        if not isinstance(blue, int):
            raise TypeError("Синий цвет должен задаваться целым числом")
        if blue < 0 or blue > 255:
            raise ValueError("Синий цвет должен задаваться неотрицательным числом меньше 256")
        self.blue = blue
        ...

    def draw_point(self, x: int, y: int) -> None:
        """
        Рисует точку с координатами x, y

        :param x: Координата x точки
        :param y: Координата y точки

        Пример:
        >>> brush = Brush(255, 0, 0, 1)
        >>> brush.draw_point(10, 10)
        """
        if not isinstance(x, int):
            raise TypeError("Координата x должна быть целым числом")
        if not isinstance(y, int):
            raise TypeError("Координата y должна быть целым числом")
        ...


if __name__ == "__main__":
    # TODO работоспособность экземпляров класса проверить с помощью doctest
    doctest.testmod()
