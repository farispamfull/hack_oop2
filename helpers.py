import random
from typing import List, Union

from items import Thing
from heroes import Paladin, Warrior

EQUIPMENT_NAMES = ('оружие', 'шлем', 'ожерелье',
                   'нагрудный доспех', 'пояс', 'сапоги')
PERSON_NAMES = ('Колинет', 'Акизан', 'Эделин', 'Делгиул', 'Киришима',
                'Драсам', 'Кхатьиеx', 'Восциx', 'Греаес', 'Миахира',
                'Бренград', 'Гнидеасам', 'Ехнеатх', 'Эделин', 'Гусусир',
                'Эзекил', 'Гаррет', 'Хемон', 'Хартен', 'Xагвеоx')


def make_heroes(number: int) -> List[Union[Paladin, Warrior]]:
    heroes = []
    for _ in range(number):
        person = random.choice((Paladin, Warrior))
        heroes.append(
            person(
                random.choice(PERSON_NAMES),
                random.randint(200, 800),
                random.randint(150, 300),
                round(random.uniform(0.01, 0.1), 2)
            )
        )
    return heroes


def make_things(number: int) -> List[Thing]:
    equipments = []
    for _ in range(number):
        equipments.append(
            Thing(
                random.choice(EQUIPMENT_NAMES),
                random.randint(50, 150),
                round(random.uniform(0.01, 0.1), 2),
                random.randint(50, 150)
            )
        )
    return equipments
