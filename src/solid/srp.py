from typing import List


# Single Responsibility Principle
# separate the concerns of the class into different classes and modules
# each class should have only one responsibility and should not have more than one reason to change
# the class should be small and focused on a single task or responsibility


class Journal:
    """Journal class"""
    def __init__(self):
        self.entries = []
        self.count = 0

    def add_entry(self, text: str) -> None:
        """Add entry to journal"""
        self.count += 1
        self.entries.append(f'{self.count}: {text}')

    def remove_entry(self, pos: int) -> None:
        """Remove entry from journal"""
        del self.entries[pos]

    def __str__(self) -> str:
        return '\n'.join(self.entries)


class PersistenceManager:
    """Persistence Manager class"""
    @staticmethod
    def save_to_file(filename: str, journal: List) -> None:
        """Save journal to file"""
        with open(filename, 'w', encoding="utf8") as file:
            file.write(str(journal))

    # def load(self, filename):
    #     """Load journal from file"""

    # def load_from_web(self, uri):
    #     """Load journal from web"""

if __name__ == '__main__':
    j = Journal()
    j.add_entry('I cried today.')
    j.add_entry('I ate a bug.')
    print(f'Journal entries: {j}')
    file_name = "./src/solid_design_pattern/journal.txt"
    PersistenceManager.save_to_file(journal=j, filename=file_name)