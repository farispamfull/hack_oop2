import random

import colorama

from game_objects.items import Item
from game_objects.characters import Paladin, Warrior, Rogue
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

if __name__ == '__main__':
    colorama.init()
    characters = CustomList([random.choice(CLASSES)() for _ in range(20)])

    for character in characters:
        character.set_items([Item() for _ in range(random.randint(0, MAX_ITEMS_PER_CHARACTER))])

    while len(characters) > 1:
        defencing_character = characters.random_pop()
        attacking_character = random.choice(characters)
        attack_description = random.choice(MOVE_DESCRIPTION)
        defence_description = random.choice(MOVE_DESCRIPTION)

        print(
            colorama.Fore.BLACK + colorama.Back.YELLOW +
            f'{attacking_character} {attack_description} attacks {defencing_character}:'
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


