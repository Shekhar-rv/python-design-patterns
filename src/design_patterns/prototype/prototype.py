from copy import deepcopy


class Address:
    def __init__(self, street_address: str, city: str, country: str):
        self.street_address = street_address
        self.city = city
        self.country = country

    def __str__(self):
        return f"{self.street_address}, {self.city}, {self.country}"


class Person:
    def __init__(self, name: str, address: Address):
        self.name = name
        self.address = address

    def __str__(self):
        return f"{self.name} lives at {self.address}"


if __name__ == "__main__":
    john = Person('John', Address('123 London Road', 'London', 'UK'))
    # This is a problem because we want to have two different addresses for John and Jane.
    # Deepcopy solves this problem without referencing the same address object.
    jane = deepcopy(john)
    jane.name = 'Jane'
    jane.address.street_address = '124 London Road'
    print(john, jane, sep='\n')
