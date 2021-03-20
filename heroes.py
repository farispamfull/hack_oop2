from typing import List, Union

from items import Thing


class Person():
    def __init__(
        self,
        name: str,
        health: int,
        attack_power: int,
        protection_percent: float
    ):
        self.name = name
        self.health = health
        self.attack_power = attack_power
        self.protection_percent = round(protection_percent, 2)
        self.equipment = []

    def _calculate_stats(self):
        for thing in self.equipment:
            self.attack_power += thing.attack
            self.health += thing.health

    def equip_gear(self, things: List[Thing]):
        for thing in things:
            print(f'{self.name} экипирован {thing.name}')
        self.equipment = things
        self._calculate_stats()

    def attack(self, enemy: Union['Paladin', 'Warrior']):
        damage = enemy.defend(self.attack_power)
        print(f'{self} наносит удар по {enemy} на {damage} урона')

    def defend(self, attack_damage: int) -> float:
        final_protection = self.protection_percent + sum(
            [item.protection_percent for item in self.equipment]
        )
        damage = round(attack_damage - (attack_damage * final_protection), 2)
        if damage > 0:
            self.health = self.health - damage
            if self.health < 0:
                self.health = 0
        return damage

    def is_dead(self) -> bool:
        return self.health <= 0

    def __str__(self):
        return self.name


class Paladin(Person):
    def __init__(
        self,
        name: str,
        health: int,
        attack_power: int,
        protection_percent: int
    ):
        super().__init__(name, health*2, attack_power, protection_percent*2)

    def __repr__(self):
        return (
            f'Paladin({self.name!r}, {self.health}, '
            f'{self.attack_power}, {self.protection_percent})'
        )


class Warrior(Person):
    def __init__(
        self,
        name: str,
        health: int,
        attack_power: int,
        protection_percent: int
    ):
        super().__init__(name, health, attack_power*2, protection_percent)

    def __repr__(self):
        return (
            f'Warrior({self.name!r}, {self.health}, '
            f'{self.attack_power}, {self.protection_percent})'
        )
