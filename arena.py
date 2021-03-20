import random
from typing import List, Union

from heroes import Paladin, Warrior


class Arena():
    def __init__(self, heroes: List[Union[Paladin, Warrior]]):
        self.heroes = heroes

    def fight(self):
        print("Добро пожаловать на Арену!")
        while len(self.heroes) > 1:
            hero_1, hero_2 = self.heroes[:2]
            print(f'{hero_1} будет сражаться с {hero_2}')

            while (not hero_1.is_dead() and not hero_2.is_dead()):
                hero_1.attack(hero_2)
                if not hero_2.is_dead():
                    hero_2.attack(hero_1)

            died = hero_1 if hero_1.is_dead() else hero_2
            print(f'Проигравший: {died}')
            self.heroes.remove(died)
            random.shuffle(self.heroes)
