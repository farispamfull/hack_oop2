import random

from game_objects.items import Item
from game_objects.characters import Paladin, Warrior
from utils import CustomList

CLASSES = (
    Paladin,
    Warrior,
)

MAX_ITEMS_PER_CHARACTER = 4

if __name__ == '__main__':
    characters = CustomList([random.choice(CLASSES)() for _ in range(20)])

    for character in characters:
        character.set_items([Item() for _ in range(random.randint(0, MAX_ITEMS_PER_CHARACTER))])

    while len(characters) > 1:
        defencing_character = characters.random_pop()
        attacking_character = random.choice(characters)

        print(f'{attacking_character} наносит удар по {defencing_character} на {attacking_character.power} урона.')
        if defencing_character.take_damage(attacking_character.power):
            print(f'{defencing_character} c честью держит удар.')
            characters.append(defencing_character)
        else:
            print(f'{defencing_character} позорно погибает.')
            del defencing_character

    print(f'{characters[0]} победил!')


