import random

def singleton(class_):
    """A decorator to create a singleton class."""
    instances = {}

    def get_instance(*args, **kwargs):
        if class_ not in instances:
            instances[class_] = class_(*args, **kwargs)
        return instances[class_]

    return get_instance


@singleton
class Database:
    def __init__(self):
        self.id = random.randint(1, 101)
        print(f"Loading database with id={self.id}")


if __name__ == "__main__":
    # The database will be loaded only once with a random id
    db1 = Database()
    db2 = Database()
    print(db1 == db2)  # True
    print(db1 is db2)  # True
    print(id(db1) == id(db2))  # True
