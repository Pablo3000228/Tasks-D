from datetime import date


class Book:
    def __init__(self, title: str, author: str, year: int):
        print("Книга добавлена!")
        self.title = title
        self.author = author
        self.year = year

    def info(self) -> str:
        return f"Название: {self.title}\nАвтор: {self.author}\nГод выпуска: {self.year}"

    def __str__(self):
        return self.info()

    def __eq__(self, other):
        return isinstance(other, Book) and self.title == other.title

    @property
    def age(self):
        return date.today().year - self.year

    @classmethod
    def from_string(cls, data):
        title, author, year = data.split(";")
        return cls(title, author, int(year))


class Ebook(Book):
    def __init__(self, title: str, author: str, year: int, format: str):
        super().__init__(title, author, year)
        self.format = format

    def info(self) -> str:
        return f"{super().info()}\nФормат: {self.format}"
