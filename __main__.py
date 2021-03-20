import random

import colorama

from game_objects.characters import Paladin, Rogue, Warrior
from game_objects.items import Item
from game_objects.utils import AttackStatus
from utils import CustomList

CLASSES = (
    Paladin,
    Warrior,
    Rogue,
)

MAX_ITEMS_PER_CHARACTER = 4

MOVE_DESCRIPTION = (
    'blindly',
    'gracelessly',
    'gracefully',
    'shamefully',
    'gloriously',
    'loudly',
    'silently',
    'beautifully',
    'shamelessly',
)

COLORS = (
    colorama.Back.GREEN,
    colorama.Back.YELLOW,
    colorama.Back.WHITE,
    colorama.Back.CYAN,
    colorama.Back.BLUE,
    colorama.Back.RED,
    colorama.Back.MAGENTA,
)

if __name__ == '__main__':
    colorama.init()
    characters = CustomList([random.choice(CLASSES)() for _ in range(20)])

    print(
        'Greetings, Your Majesty! '
        'Welcome to our tournament!\n'
        'Our champions for today are:\n'
    )
    for character in characters:
        background_color = random.choice(COLORS)
        character.set_items(
            [Item() for _ in range(random.randint(0, MAX_ITEMS_PER_CHARACTER))]
        )
        print(
            f'{character.get_full_name()}'
        )
    print('Sir, would you like to interact with champions? [YES/NO]\n'
          'Press NO for auto fight.')
    is_interactive_fight = input().upper()
    if is_interactive_fight == 'YES':
        print('Great choice!\n'
              'Here are some commands you can use:\n'
              'heal <character name> - restore 50 HP to specified character\n'
              'kill <character name> - kill specified character\n'
              'drop_bomb - damage all characters on 25 HP\n'
              'stole_item <character name>\n'
              'press any button to skip\n')
    while len(characters) > 1:
        if is_interactive_fight == 'YES':
            print('Make decision, Sir!')
            commands = input().split()
            if commands[0] == 'heal':
                character_name = commands[1]
                for character in characters:
                    if character.name == character_name:
                        character.health += 50
            elif commands[0] == 'drop_bomb':
                for character in characters:
                    status = character.take_damage(25)
                    if status is AttackStatus.KILL:
                        description = random.choice(MOVE_DESCRIPTION)
                        print(
                            colorama.Fore.RED +
                            f'{character} {description} dies.' +
                            colorama.Style.RESET_ALL
                        )
                        del character
            elif commands[0] == 'kill':
                character_name = commands[1]
                for character in characters:
                    if character.name == character_name:
                        description = random.choice(MOVE_DESCRIPTION)
                        print(
                            colorama.Fore.RED +
                            f'{character} {description} dies.' +
                            colorama.Style.RESET_ALL
                        )
                        del character
            elif commands[0] == 'stole_item':
                character_name = commands[1]
                for character in characters:
                    if character.name == character_name:
                        log = character.remove_random_item()
                        print(f'{character} loses:\n', log)

        defencing_character = characters.random_pop()
        attacking_character = random.choice(characters)
        attack_description = random.choice(MOVE_DESCRIPTION)
        defence_description = random.choice(MOVE_DESCRIPTION)

        print(
            colorama.Fore.BLACK + colorama.Back.YELLOW +
            f'{attacking_character} {attack_description} '
            f'attacks {defencing_character}:'
            f' {attacking_character.power} hit points.' +
            colorama.Style.RESET_ALL
        )

        status = defencing_character.take_damage(attacking_character.power)

        if status is AttackStatus.HIT:
            print(
                colorama.Fore.BLUE +
                f'{defencing_character} {defence_description} stands.' +
                colorama.Style.RESET_ALL
            )
            characters.append(defencing_character)
        elif status is AttackStatus.KILL:
            print(
                colorama.Fore.RED +
                f'{defencing_character} {defence_description} dies.' +
                colorama.Style.RESET_ALL
            )
            del defencing_character
        elif status is AttackStatus.DODGE:
            print(
                colorama.Fore.GREEN +
                f'{defencing_character} {defence_description} dodges attack.' +
                colorama.Style.RESET_ALL
            )

    win_description = random.choice(MOVE_DESCRIPTION)
    print(
        colorama.Fore.BLACK + colorama.Back.GREEN +
        f'{characters[0]} {win_description} wins!' +
        colorama.Style.RESET_ALL
    )
