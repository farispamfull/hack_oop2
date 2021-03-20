import json
from random import choice, randrange

from character import Paladin, Warrior
from item import Item


def sort_defence(item):
    print('СортировОчка')
    return item.defence


class Game():
    NAMES = ['Добрыня', 'Иван', 'Зена', 'Сабзиро', 'Ибрагим', 'Олимпия', 'Боб',
             'Артемис', 'Апполинария', 'Арес', 'Гвиневра', 'Теренитий']
    CHARACTER_TYPES = ['Paladin', 'Warrior']
    ITEM_TYPES = []
    item_list = json.load(open('items.json', encoding='utf-8'))
    for item in item_list:
        ITEM_TYPES.append(Item(item_list[item], mode='dict'))

    def __init__(self):
        self.characters = []
        self.dead_characters = []
        self.items = []

    def show_characters(self):
        return 'Чемпионы:\n'+'\n'.join(str(character)
                                       for character in self.characters)

    def show_items(self):
        return 'Предметы:\n'+'\n'.join(str(item) for item in self.items)

    def generate_set_of_characters(self, amount):
        for i in range(amount):
            self.characters.append(self.generate_character())

    def generate_character(self):
        name = choice(self.NAMES)
        attack = randrange(7, 25)
        defence = randrange(0, 10)
        hp = randrange(30, 100)
        type = choice(self.CHARACTER_TYPES)
        if type == 'Paladin':
            return Paladin(hp, attack, defence, name)
        elif type == 'Warrior':
            return Warrior(hp, attack, defence, name)
        else:
            return None

    def give_items(self):
        pass

    def generate_set_of_items(self, amount):
        for i in range(amount):
            self.items.append(choice(self.ITEM_TYPES))
        self.items = sorted(self.items, key=lambda x: x.defence)
