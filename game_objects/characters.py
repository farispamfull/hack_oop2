import random
from dataclasses import dataclass
from typing import Optional

from game_objects.items import Item

NAMES = (
    'Arthur',
    'Alexander',
    'Bagdemagus',
    'Bedivere',
    'Bors',
    'Brunor',
    'Cligès',
    'Caradoc',
    'Dagonet',
    'Daniel',
    'Dinadan',
    'Galahad',
    'Galehaut',
    'Geraint',
    'Griflet',
    'Lamorak',
    'Lancelot',
    'Lanval',
    'Lionel',
    'Moriaen',
    'Palamedes',
    'Pelleas',
    'Pellinore',
    'Percival',
    'Sagramore',
    'Tristan',
)


@dataclass
class Person:
    equipped_items: Optional[list[Item]] = None
    health: int = 100
    power: int = 15
    armor: float = 0.1
    cls: str = 'person'

    def __post_init__(self):
        self.name = random.choice(NAMES)

    def __str__(self) -> str:
        return f'{self.name} ({self.cls})'

    # def __str__(self) -> str:
    #     if self.equipped_items:
    #         item_names = ', '.join([item.name for item in self.equipped_items])
    #     else:
    #         item_names = 'nothing'
    #
    #     return (
    #         f'{self.name} ({self.cls}).\n'
    #         f'Equipped with {item_names}.\n'
    #     )

    def take_damage(self, damage) -> bool:
        self.health -= damage * (1 - self.armor)
        if self.health <= 0:
            return False
        return True

    def set_items(self, items: list[Item]) -> None:
        self.equipped_items = items
        for item in items:
            self.health += item.health
            self.armor += item.armor
            self.power += item.power


class Paladin(Person):
    cls: str = 'paladin'

    def __init__(self):
        super().__init__()
        self.health *= 2
        self.armor *= 2


class Warrior(Person):
    cls: str = 'warrior'

    def __init__(self):
        super().__init__()
        self.power *= 2
