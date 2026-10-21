"""Модель онлайн-магазина: товары, корзина, покупатель и заказ."""


class Product:
    """Товар магазина.

    Attributes:
        name (str): Название товара.
        price (float): Цена за штуку.
        stock (int): Количество на складе.
        category (str): Категория товара.
    """

    def __init__(self, name, price, stock, category):
        self.name = name
        self.price = price
        self.stock = stock
        self.category = category


class ShoppingCart:
    """Корзина покупателя.

    Attributes:
        items (dict): Товары в корзине в виде {Product: количество}.
    """

    def __init__(self):
        self.items = {}

    def add_product(self, product, quantity=1):
        """Добавить товар в корзину, если его хватает на складе.

        Args:
            product (Product): Добавляемый товар.
            quantity (int): Количество.
        """
        in_cart = self.items.get(product, 0)
        if in_cart + quantity > product.stock:
            print(f"Недостаточно товара «{product.name}» на складе")
            return
        self.items[product] = in_cart + quantity

    def remove_product(self, product):
        """Убрать товар из корзины.

        Args:
            product (Product): Удаляемый товар.
        """
        self.items.pop(product, None)

    def update_quantity(self, product, quantity):
        """Изменить количество товара в корзине.

        Args:
            product (Product): Товар в корзине.
            quantity (int): Новое количество, 0 - убирает товар из корзины.
        """
        if quantity <= 0:
            self.remove_product(product)
        elif quantity <= product.stock:
            self.items[product] = quantity
        else:
            print(f"Недостаточно товара «{product.name}» на складе")

    def get_total(self):
        """Посчитать стоимость корзины без скидок и налогов.

        Returns:
            float: Сумма цен всех товаров в корзине.
        """
        return sum(product.price * quantity for product, quantity in self.items.items())


class Customer:
    """Покупатель магазина.

    Attributes:
        name (str): Имя покупателя.
        cart (ShoppingCart): Корзина покупателя.
        orders (list[Order]): История заказов.
    """

    def __init__(self, name):
        self.name = name
        self.cart = ShoppingCart()
        self.orders = []


class Order:
    """Заказ, оформленный из корзины покупателя.

    Attributes:
        customer (Customer): Покупатель.
        items (dict): Копия товаров из корзины {Product: количество}.
        discount (float): Скидка в процентах.
        tax (float): Налог в процентах.
    """

    def __init__(self, customer, discount=0, tax=0):
        self.customer = customer
        self.items = dict(customer.cart.items)
        self.discount = discount
        self.tax = tax

    def calculate_total(self):
        """Посчитать итоговую цену: сначала скидка, потом налог.

        Returns:
            float: Итоговая стоимость заказа.
        """
        subtotal = sum(
            product.price * quantity for product, quantity in self.items.items()
        )
        return subtotal * (1 - self.discount / 100) * (1 + self.tax / 100)

    def place(self):
        """Оформить заказ: списать товары со склада, сохранить
        заказ в истории покупателя и очистить корзину."""
        for product, quantity in self.items.items():
            product.stock -= quantity
        self.customer.orders.append(self)
        self.customer.cart.items.clear()
