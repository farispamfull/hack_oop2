import json
from random import choice, randint, randrange

import colorama

from character import Paladin, Warrior
from item import Item

colorama.init(autoreset=True)


class Game():
    CHARACTER_TYPES = ['Paladin', 'Warrior']
    ITEM_TYPES = []
    item_list = json.load(open('items.json', encoding='utf-8'))
    for item in item_list:
        ITEM_TYPES.append(Item(item_list[item], mode='dict'))

    def __init__(self):
        self.names = ['Добрыня', 'Иван', 'Зенон', 'Сабзиро', 'Ибрагим',
                      'Олимпиец', 'Боб', 'Артемис', 'Апполинарий', 'Арес',
                      'Гвиневр', 'Теренитий', 'Валера']
        self.characters = []
        self.dead_characters = []
        self.items = []
        self.round_number = 0
        self.damage_dealt = 0

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
        self.round_number += 1
        print(f'Paунд {self.round_number}')
        for character in self.characters:
            enemies = self.characters.copy()
            enemies.remove(character)
            target_character = choice(enemies)
            recieved = target_character.recieve_damage(character.get_damage())
            if recieved == 'Dead':
                self.dead_characters.append(target_character)
                self.characters.remove(target_character)
                print(colorama.Fore.RED + f'{character.name} атакует '
                      f'{target_character.name} и убивает его!')
            else:
                self.damage_dealt += recieved
                print(colorama.Fore.WHITE + f'{character.name} атакует '
                      f'{target_character.name} и наносит {recieved} урона!')
        print()

    def play(self):
        while (len(self.characters) > 1):
            self.round()

    def anounce_results(self):
        champion = max(self.characters, key=lambda x: x.current_hp)
        print(colorama.Fore.YELLOW + f'И победитель этой битвы! В которой было'
                                     f' нанесено {self.damage_dealt} урона!!\n'
                                     f'{champion.show_full_stats()}\n'
                                     f'А вот и его вещи:\n'
                                     f'{champion.show_inventory()}\n')
        print(colorama.Fore.CYAN +
              'Покойтесь с миром:\n' +
              '\n'.join(char.show_title() for char in self.dead_characters))
