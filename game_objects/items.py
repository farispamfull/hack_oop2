import random

from game_objects.utils import DESCRIPTION

ITEM_TYPES = (
    'ring',
    'belt',
    'vest',
    'sword',
    'shield',
    'axe',
    'hammer',
    'trinket',
    'dagger',
)

ITEM_RELATION = (
    'Thunder',
    'Foolness',
    'Power',
    'Stumble',
    'Wall',
    'Fountain',
    'Teapot',
    'Freakness',
    'Shameless',
)


class Item:
    def __init__(self) -> None:
        self.type = random.choice(ITEM_TYPES)
        self.armor = round(random.uniform(0, 0.1), 2)
        self.health = random.randint(0, 5)
        self.power = random.randint(0, 5)
        self.name = f'{DESCRIPTION} {self.type} of {ITEM_RELATION}'

    def get_full_description(self) -> str:
        return (
            f'Item name: {self.name}\n'
            f'Armor: {self.armor}\n'
            f'Health: {self.health}\n'
            f'Power: {self.power}\n'
        )

    def __str__(self):
        return self.name
