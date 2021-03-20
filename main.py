import random

from arena import Arena
from helpers import make_heroes, make_things


def main():
    equipments = make_things(10)
    equipments.sort(key=lambda x: x.protection_percent)

    heroes = make_heroes(10)
    for hero in heroes:
        equipments_for_hero = random.choices(
            equipments,
            k=random.randint(1, 4)
        )
        hero.equip_gear(equipments_for_hero)

    arena = Arena(heroes)
    arena.fight()


if __name__ == '__main__':
    main()
