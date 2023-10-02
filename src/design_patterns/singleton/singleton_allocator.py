import random


class Database:
    _instance = None

    def __init__(self):
        id = random.randint(1, 101)
        print(f"Loading database with id={id}")

    def __new__(self, *args, **kwargs):
        if not self._instance:
            self._instance = super(Database, self).__new__(self, *args, **kwargs)
        return self._instance


if __name__ == "__main__":
    # The database will be loaded twice with different ids
    # because the __init__ method is called twice.
    db1 = Database()
    db2 = Database()
    print(db1 == db2)  # True
    print(db1 is db2)  # True
    print(id(db1) == id(db2))  # True
