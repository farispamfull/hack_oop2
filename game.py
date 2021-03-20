import json
from random import choice, randint, randrange

from character import Paladin, Warrior
from item import Item


class Game():
    CHARACTER_TYPES = ['Paladin', 'Warrior']
    ITEM_TYPES = []
    item_list = json.load(open('items.json', encoding='utf-8'))
    for item in item_list:
        ITEM_TYPES.append(Item(item_list[item], mode='dict'))

    def __init__(self):
        self.names = ['Добрыня', 'Иван', 'Зена', 'Сабзиро', 'Ибрагим',
                      'Олимпия', 'Боб', 'Артемис', 'Апполинария', 'Арес',
                      'Гвиневра', 'Теренитий', 'Валера']
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
        name = choice(self.names)
        self.names.remove(name)
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
        last_items = len(self.items)
        for character in self.characters:
            number_of_items = randint(0, 4 if last_items > 4 else last_items)
            last_items -= number_of_items
            for i in range(number_of_items):
                item = choice(self.items)
                character.add_item(item)
                self.items.remove(item)

    def generate_set_of_items(self, amount):
        for i in range(amount):
            self.items.append(choice(self.ITEM_TYPES))
        self.items = sorted(self.items, key=lambda x: x.defence)

    def round(self):
        for character in self.characters:
            enemies = self.characters.copy()
            enemies.remove(character)
            target_character = choice(enemies)
            recieved = target_character.recieve_damage(character.get_damage())
            if recieved == 'Dead':
                self.dead_characters.append(target_character)
                self.characters.remove(target_character)
                print(f'{character.name} атакует {target_character.name} и '
                      f'убивает его!')
            else:
                print(f'{character.name} атакует {target_character.name} и '
                      f'наносит {recieved} урона!')
        print('Paунд!!!\n\n\n')

    def play(self):
        while (len(self.characters) > 1):
            self.round()
