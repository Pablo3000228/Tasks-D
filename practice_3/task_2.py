"""Описания разных видов транспорта."""


class Transport:
    """Транспортное средство.

    Attributes:
        name (str): Название транспорта.
    """

    def __init__(self, name):
        """Создать транспорт.

        Args:
            name (str): Название транспорта.
        """
        self.name = name

    def description(self):
        """Получить описание транспорта.

        Returns:
            str: Общее описание транспорта.
        """
        return "Транспорт"


class Car(Transport):
    """Автомобиль."""

    def description(self):
        """Получить описание автомобиля.

        Returns:
            str: Описание с названием автомобиля.
        """
        return f"Этот транспорт - {self.name}"


class Plane(Transport):
    """Самолёт."""

    def description(self):
        """Получить описание самолёта.

        Returns:
            str: Описание с названием самолёта.
        """
        return f"Этот транспорт - {self.name}, у него есть крылья и он высоко летает"


class Bike(Transport):
    """Мотоцикл."""

    def description(self):
        """Получить описание мотоцикла.

        Returns:
            str: Описание с названием мотоцикла.
        """
        return f"Этот транспорт - {self.name}, он совсем маленький"


plane = Plane("Boeing")
print(plane.description())
car = Car("BMW")
print(car.description())
bike = Bike("Kawasaki")
print(bike.description())
