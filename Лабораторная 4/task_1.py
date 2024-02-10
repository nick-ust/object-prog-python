class Headphones:
    """Базовый класс наушников"""
    def __init__(self, name: str, construction_type: str, color: str, volume: int = 0):
        """
        Создание и подготовка к работе класса "Наушники"

        :param name: Название наушников. Не может измениться
        :param construction_type: Тип конструкции наушников. Не может измениться
        :param color: Цвет наушников. Не может измениться
        :param volume: Громкость наушников. Должно быть целым числом от 0 до 100
        """
        self._name = name
        self._construction_type = construction_type
        self._color = color
        self.volume = volume

    @property
    def name(self) -> str:
        return self._name

    @property
    def construction_type(self) -> str:
        return self._construction_type

    @property
    def color(self) -> str:
        return self._color

    @property
    def volume(self) -> int:
        return self._volume

    @volume.setter
    def volume(self, new_volume) -> None:
        if not isinstance(new_volume, int):
            raise TypeError("Громкость должна быть типа int")
        if new_volume < 0 or new_volume > 100:
            raise ValueError("Громкость должна быть целым числом от 0 до 100")
        self._volume = new_volume

    def __str__(self) -> str:
        return f"Наушники {self.name} с конструкцией типа {self.construction_type}, цвет: {self.color}, " \
               f"текущая громкость: {self.volume}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, construction_type={self.construction_type!r}, " \
               f"color={self.color!r}, volume={self.volume!r})"

    def connect(self) -> bool:
        """Подключить наушники к устройству"""
        ...

    def disconnect(self) -> bool:
        """Отключить наушники от устройства"""
        ...

    def play(self) -> bool:
        """Воспроизвести музыку"""
        ...

    def pause(self) -> bool:
        """Поставить музыку на паузу"""
        ...


class WirelessHeadphones(Headphones):
    """Класс беспроводных наушников"""
    def __init__(self, name: str, construction_type: str, color: str, bluetooth_version: str, volume: int = 0):
        """
        Создание и подготовка к работе класса "Беспроводные наушники"

        :param bluetooth_version: Версия Bluetooth. Не может измениться
        """
        super().__init__(name, construction_type, color, volume)
        self._bluetooth_version = bluetooth_version

    @property
    def bluetooth_version(self) -> str:
        return self._bluetooth_version

    def __str__(self) -> str:
        return f"Беспроводные наушники {self.name} с конструкцией типа {self.construction_type}, " \
               f"версией Bluetooth {self.bluetooth_version}, цвет: {self.color}, текущая громкость: {self.volume}"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}(name={self.name!r}, construction_type={self.construction_type!r}, " \
               f"color={self.color!r}, bluetooth_version={self.bluetooth_version!r}, volume={self.volume!r})"

    def connect(self) -> bool:
        """Подключить наушники к устройству по Bluetooth. Отличается от базового класса типом подключения"""
        ...

    def disconnect(self) -> bool:
        """Отключить наушники от устройства. Отличается от базового класса типом подключения"""
        ...

    def toggle_noise_reduction(self) -> bool:
        """Переключить режим шумоподавления"""
        ...
