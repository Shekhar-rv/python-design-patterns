from abc import ABC, abstractmethod
from enum import Enum, auto


class HotDrink(ABC):
    @abstractmethod
    def consume(self):
        pass


class Tea(HotDrink):
    def consume(self):
        print('This tea is nice but I\'d prefer it with milk')


class Coffee(HotDrink):
    def consume(self):
        print('This coffee is delicious')


# class HotDrinkFactory(ABC):
#     @abstractmethod
#     def prepare(self, amount):
#         pass


class TeaFactory:
    def prepare(self, amount):
        print(
            'Put in tea bag, boil water,'
            f' pour {amount}ml, enjoy!'
        )
        return Tea()


class CoffeeFactory:
    def prepare(self, amount):
        print(
            'Grind some beans, boil water,'
            f' pour {amount}ml, enjoy!'
        )
        return Coffee()


def make_drink(type):
    match type:
        case 'tea':
            return TeaFactory().prepare(200)
        case 'coffee':
            return CoffeeFactory().prepare(50)
        case _:
            return None


class HotDrinkMachine:
    class AvailableDrink(Enum):
        COFFEE = auto()
        TEA = auto()

    factories = []
    initialized = False

    def __init__(self):
        if not self.initialized:
            self.initialized = True
            for d in self.AvailableDrink:
                name = d.name.title()
                factory_name = f'{name}Factory'
                factory_instance = eval(factory_name)()
                self.factories.append((name, factory_instance))

    def make_drink(self):
        print('Available drinks:')
        for f in self.factories:
            print(f[0])

        s = input(f'Please pick drink (0-{len(self.factories)-1}): ')
        idx = int(s)
        s = input('Specify amount: ')
        amount = int(s)
        return self.factories[idx][1].prepare(amount)


if __name__ == "__main__":
    hdm = HotDrinkMachine()
    hdm.make_drink()
