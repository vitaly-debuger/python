from abc import ABC, abstractmethod


class Closes(ABC):
    def __init__(self, name, count):
        self.n = name
        self.c = int(count)

    @abstractmethod
    def my_method(self):
        pass


class Coat(Closes):
    @property
    def my_method(self):
        return float((self.c / 6.5) + 0.5)


class Costume(Closes):
    @property
    def my_method(self):
        return float((self.c * 2) + 0.3)


coat_1 = Coat('Сюзанна', 42)
costume_1 = Costume('Идилия', 187)
print(f"Сумма ткани для пальто {coat_1.n} и костюма {costume_1.n} - {round(coat_1.my_method + costume_1.my_method, 2)}")
