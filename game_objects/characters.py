import random
from dataclasses import dataclass
from typing import Optional

from game_objects.items import Item
from game_objects.utils import DESCRIPTION, AttackStatus

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

TITLES = (
    'Sir',
    'Lord',
    'Duke',
    'King',
)

CHARACTER_RELATION = (
    'Schwifordshire',
    'Harlem',
    'San-Francisco',
    'PEPland',
    'Pub',
    'China',
    'Ellington',
)


@dataclass
class Person:
    equipped_items: Optional[list[Item]] = None
    health: int = 100
    power: int = 15
    armor: float = 0.1
    dodge_probability: float = 0.0
    cls: str = 'person'

    def __post_init__(self):
        self.name = random.choice(NAMES)
        self.title = random.choice(TITLES)
        self.relation = random.choice(CHARACTER_RELATION)
        self.description = random.choice(DESCRIPTION)

    def __str__(self) -> str:
        return (f'{self.title} {self.description} {self.name} '
                f'of {self.relation}')

    def get_full_name(self) -> str:
        if self.equipped_items:
            item_names = '\n'.join([item.get_full_description()
                                    for item in self.equipped_items])
        else:
            item_names = 'nothing'

        return (
            f'{self}.\n'
            f'Class: {self.cls}\n'
            f'Equipped with\n'
            f'{item_names}\n'
        )

    def take_damage(self, damage) -> AttackStatus:
        dice = random.random()
        if dice <= self.dodge_probability:
            return AttackStatus.DODGE
        self.health -= damage * (1 - self.armor)
        if self.health <= 0:
            return AttackStatus.KILL
        return AttackStatus.HIT

    def set_items(self, items: list[Item]) -> None:
        self.equipped_items = items
        for item in items:
            self.health += item.health
            self.armor += item.armor
            self.power += item.power

    def remove_random_item(self) -> str:
        if self.equipped_items:
            r_item = self.equipped_items.pop()
            self.health -= r_item.health
            self.power -= r_item.power
            self.armor -= r_item.armor
            return f'{r_item}'
        return 'nothing to remove'


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


class Rogue(Person):
    cls: str = 'rogue'
    dodge_probability: float = 0.5
