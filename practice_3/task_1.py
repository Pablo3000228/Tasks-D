"""Расчёт зарплат сотрудников разных должностей."""


class Employee:
    """Обычный сотрудник с фиксированным окладом.

    Attributes:
        id (int): Идентификатор сотрудника.
        name (str): Имя сотрудника.
        base_money (int): Базовый оклад.
    """

    def __init__(self, id, name, base_money):
        """Создать сотрудника.

        Args:
            id (int): Идентификатор сотрудника.
            name (str): Имя сотрудника.
            base_money (int): Базовый оклад.
        """
        self.id = id
        self.name = name
        self.base_money = base_money

    def calculate_salaries(self):
        """Посчитать зарплату сотрудника.

        Returns:
            int: Зарплата, равная базовому окладу.
        """
        return self.base_money


class Manager(Employee):
    """Менеджер: к окладу добавляется фиксированный бонус.

    Attributes:
        bonus (int): Бонус к окладу.
    """

    def __init__(self, id, name, base_money, bonus):
        """Создать менеджера.

        Args:
            id (int): Идентификатор сотрудника.
            name (str): Имя сотрудника.
            base_money (int): Базовый оклад.
            bonus (int): Бонус к окладу.
        """
        super().__init__(id, name, base_money)
        self.bonus = bonus

    def calculate_salaries(self):
        """Посчитать зарплату менеджера.

        Returns:
            int: Сумма базового оклада и бонуса.
        """
        return self.base_money + self.bonus


class Developer(Employee):
    """Разработчик: к окладу добавляется 10000 за каждый проект.

    Attributes:
        project_sum (int): Количество проектов.
    """

    def __init__(self, id, name, base_money, project_sum):
        """Создать разработчика.

        Args:
            id (int): Идентификатор сотрудника.
            name (str): Имя сотрудника.
            base_money (int): Базовый оклад.
            project_sum (int): Количество проектов.
        """
        super().__init__(id, name, base_money)
        self.project_sum = project_sum

    def calculate_salaries(self):
        """Посчитать зарплату разработчика.

        Returns:
            int: Базовый оклад плюс 10000 за каждый проект.
        """
        return self.base_money + self.project_sum * 10000


emp_alex = Employee(0, "Alex", 50000)
manager_ivan = Manager(1, "Ivan", 50000, 10000)
dev_eva = Developer(2, "Eva", 50000, 5)

print(emp_alex.calculate_salaries())
print(manager_ivan.calculate_salaries())
print(dev_eva.calculate_salaries())
