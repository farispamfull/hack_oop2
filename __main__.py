import random

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
    characters = CustomList([random.choice(CLASSES)() for _ in range(20)])

    for character in characters:
        character.set_items([Item() for _ in range(random.randint(0, MAX_ITEMS_PER_CHARACTER))])

    while len(characters) > 1:
        defencing_character = characters.random_pop()
        attacking_character = random.choice(characters)
        attack_description = random.choice(MOVE_DESCRIPTION)
        defence_description = random.choice(MOVE_DESCRIPTION)

        print(f'{attacking_character} {attack_description} attacks {defencing_character}:'
              f' {attacking_character.power} hit points.')
        status = defencing_character.take_damage(attacking_character.power)
        if status is AttackStatus.HIT:
            print(f'{defencing_character} {defence_description} stands.')
            characters.append(defencing_character)
        elif status is AttackStatus.KILL:
            print(f'{defencing_character} {defence_description} dies.')
            del defencing_character
        elif status is AttackStatus.DODGE:
            print(f'{defencing_character} {defence_description} dodges attack.')

    win_description = random.choice(MOVE_DESCRIPTION)
    print(f'{characters[0]} {win_description} wins!')


