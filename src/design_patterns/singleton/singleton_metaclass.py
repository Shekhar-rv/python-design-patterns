import random


class Singleton(type):
    _instances = {}

    def __call__(self, *args, **kwargs):
        if self not in self._instances:
            self._instances[self] = super(Singleton, self).__call__(*args, **kwargs)
        return self._instances[self]


class Database(metaclass=Singleton):
    def __init__(self):
        id = random.randint(1, 101)
        print(f"Loading database with id: {id}")


if __name__ == "__main__":
    # The database will be loaded only once with a random id
    db1 = Database()
    db2 = Database()
    print(db1 == db2)  # True
    print(db1 is db2)  # True
    print(id(db1) == id(db2))  # True