"""Симулятор управления космическим кораблём."""

import random


class Spaceship:
    """Космический корабль.

    Attributes:
        fuel (float): Запас топлива в литрах.
        state (float): Целостность корпуса в процентах (0–100).
        speed (float): Текущая скорость в км/с.
    """

    def __init__(self, fuel: float, speed: float, state=100):
        """Создать корабль.

        Args:
            fuel (float): Запас топлива в литрах.
            speed (float): Начальная скорость в км/с.
            state (float): Целостность корпуса в процентах.
        """
        self.fuel = fuel
        self.state = state
        self.speed = speed

    def print_info(self):
        """Напечатать топливо, целостность и скорость корабля."""
        print("Корабль:")
        print(f"Оставшееся топливо (л.): {self.fuel}")
        print(f"Целостность (%): {self.state}")
        print(f"Текущая скорость (км/с): {self.speed}")
        print()

    def accelerate(self, amount: float):
        """Разогнать корабль, потратив столько же топлива.

        Args:
            amount (float): На сколько увеличить скорость.
        """
        if amount > self.fuel:
            print("Не хватает топлива до разгона!")
            return
        self.fuel -= amount
        self.speed += amount

    def damage(self, damage: float):
        """Повредить корпус; целостность не опускается ниже 0.

        Args:
            damage (float): Величина повреждения в процентах.
        """
        if damage > self.state:
            print("Корабль сломан!")
            self.state = 0
            return
        self.state -= damage

    def repair(self, amount: float):
        """Починить корпус; целостность не поднимается выше 100.

        Args:
            amount (float): На сколько процентов восстановить корпус.
        """
        if amount + self.state >= 100:
            print("Корабль полностью исправен!")
            self.state = 100
            return
        self.state += amount


class CrewMember:
    """Член экипажа.

    Attributes:
        name (str): Имя.
        role (str): Роль в команде, например "Пилот" или "Инженер".
        skills (list[str]): Навыки.
        health (float): Здоровье (0 — погиб).
    """

    def __init__(self, name, role, skills, health=100):
        """Создать члена экипажа.

        Args:
            name (str): Имя.
            role (str): Роль в команде.
            skills (list[str]): Навыки.
            health (float): Начальное здоровье.
        """
        self.name = name
        self.role = role
        self.skills = skills
        self.health = health

    def damage(self, damage: float):
        """Нанести урон; здоровье не опускается ниже 0.

        Args:
            damage (float): Величина урона.
        """
        if damage >= self.health:
            print("Член экипажа погиб.")
            self.health = 0
            return
        self.health -= damage

    def treatment(self, amount: float):
        """Вылечить; здоровье не поднимается выше 100.

        Args:
            amount (float): На сколько восстановить здоровье.
        """
        if amount + self.health >= 100:
            print("Член экипажа полностью восстановился!")
            self.health = 100
            return
        self.health += amount


class Mission:
    """Миссия корабля с экипажем и случайными событиями.

    Attributes:
        goal (str): Цель миссии.
        ship (Spaceship): Корабль.
        crew (list[CrewMember]): Экипаж.
    """

    def __init__(self, goal, ship, crew):
        """Создать миссию.

        Args:
            goal (str): Цель миссии.
            ship (Spaceship): Корабль.
            crew (list[CrewMember]): Экипаж.
        """
        self.goal = goal
        self.ship = ship
        self.crew = crew

    def find_crewmember(self, role):
        """Найти живого члена экипажа с нужной ролью.

        Args:
            role (str): Роль, например "Пилот".

        Returns:
            CrewMember | None: Найденный член экипажа или None, если такого нет.
        """
        for member in self.crew:
            if member.role == role and member.health != 0:
                return member

    def asteroid(self):
        """Столкновение с астероидом: урон кораблю, живой пилот уменьшает его вдвое."""
        print("Попадание астероида!")
        damage = random.randint(20, 40)
        if self.find_crewmember("Пилот"):
            print("Пилот спас ситуацию - урон урезан в 2 раза.")
            damage //= 2
        self.ship.damage(damage)
        print()

    def accident(self):
        """Авария: ранит случайного живого члена экипажа, живой инженер чинит корабль."""
        print("Авария!")
        alive = [member for member in self.crew if member.health > 0]
        if not alive:
            print("Экипаж погиб, пострадать некому.")
            return
        member = random.choice(alive)
        damage = random.randint(20, 40)
        member.damage(damage)
        print(f"Ранен: {member.name}, текущее здоровье: {member.health}")
        engineer = self.find_crewmember("Инженер")
        if engineer:
            self.ship.repair(15)
            print(f"{engineer.name} чинит корабль: {self.ship.state}")
        print()

    def start(self, fuel_needed, events=2):
        """Запустить миссию: разгон, случайные события и итог.

        Args:
            fuel_needed (float): Сколько топлива нужно на миссию.
            events (int): Количество случайных событий в полёте.

        Returns:
            bool | None: True, если миссия выполнена, иначе None.
        """
        print(f"Миссия начата!\n Цель: {self.goal}\n")
        self.ship.print_info()
        if fuel_needed > self.ship.fuel:
            print("Текущего топлива недостаточно.")
            return
        self.ship.accelerate(fuel_needed)

        for _ in range(events):
            random.choice([self.accident, self.asteroid])()
            if self.ship.state == 0:
                print("Корабль уничтожен. Миссия провалена!")
                return
        print("Все возможные события пережиты.")

        alive = [member.role for member in self.crew if member.health > 0]
        if not alive:
            print("Экипаж погиб. Миссия провалена!")
            return

        print(
            f"Миссия успешно выполнена! \nТекущая скорость: {self.ship.speed}\n"
            f"Оставшееся топливо: {self.ship.fuel}\n Выжившие: {', '.join(alive)}"
        )
        return True


ship = Spaceship(200000, 120, 100)
crew = [
    CrewMember("Димон", "Пилот", ["Пилотирование", "Навигация", "Первая помощь"]),
    CrewMember("Жора", "Инженер", ["Ремонт корабля", "Первая помощь"]),
]
mission = Mission("Колонизация новой планеты", ship, crew)
mission.start(30000)
