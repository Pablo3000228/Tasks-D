class Transport:
    def __init__(self, name):
        self.name = name

    def description(self):
        return "Транспорт"


class Car(Transport):
    def description(self):
        return f"Этот транспорт - {self.name}"


class Plane(Transport):
    def description(self):
        return f"Этот транспорт - {self.name}, у него есть крылья и он высоко летает"


class Bike(Transport):
    def description(self):
        return f"Этот транспорт - {self.name}, он совсем маленький"


plane = Plane("Boeing")
print(plane.description())
