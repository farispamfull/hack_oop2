import random

ITEMS = (
    'ring',
    'belt',
    'vest',
    'sword',
    'shield',
    'axe',
    'hammer',
    'trinket',
)


class Item:
    def __init__(self) -> None:
        self.name = random.choice(ITEMS)
        self.armor = round(random.uniform(0, 0.1), 2)
        self.health = random.randint(0, 5)
        self.power = random.randint(0, 5)

    def __str__(self) -> str:
        return (
            f'Item name: {self.name}\n'
            f'Armor: {self.armor}\n'
            f'Health: {self.health}\n'
            f'Power: {self.power}\n'
        )

    # def __cmp__(self, other) -> bool:
    #     return self.armor > other.armor
