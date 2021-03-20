import random
import argparse

TEXT = {
    'attack': ('{attacker_name} ({attacker_class}) '
               'с атакой в {attacker_attack} единиц '
               'наносит удар по '
               '{defender_name} ({defender_class} '
               'health={defender_health_bef}) '
               'на {attacker_attack} единиц урона. '
               'У {defender_name} остается {defender_health_aft} '
               'пунктов жизни.'),
    'dead': '{name} ({player_type}) был убит.',
    'winner': '{name} ({winner_type}) побеждает со здоровьем в {health}!',
    'error_player_not_found': ('Заданная Вами раса {kind} не существует.'
                               'Выбираю default персонаж.')
}
ROUND_RESULTS = 2


def round_wrapper(value):
    return int(value) if value == 0 else round(value, ROUND_RESULTS)


def roll_dice(n=20):
    """
    Generate randomness
    :param n: number to check on a dice.
    :return: True if you are lucky.
    """
    return True if random.randint(1, n) == n else False


class Things:
    MAX_DEFEND = 0.1

    def __init__(self, name: str, defend, attack, health):
        """
        :param name: Str name of a thing.
        :param defend: Defend ratio.
        :param attack: Attack points.
        :param health: Health points.
        """
        self.name = name
        self.defend = defend if defend <= self.MAX_DEFEND else self.MAX_DEFEND
        self.attack = attack
        self.health = health

    def __str__(self):
        return (f'{self.name} '
                f'-- {self.__class__.__name__} -- '
                f'defend = {self.defend}, '
                f'attack = {self.attack}, '
                f'health = {self.health}.')

    def __repr__(self):
        return f'{self.name}'


class Person:
    # Max things person can hold.
    THINGS_NUM = 4
    # coefficients to be applied when the Thing is worn,
    # i.e. the specific person increases specific property
    COEFFICIENTS = {
        'DEFEND_COEFFICIENT': 1.,
        'HEALTH_COEFFICIENT': 1.,
        'ATTACK_COEFFICIENT': 1.
    }
    # Number of numeric params for further instances auto generation
    PARAMS_NUM = 3

    def __init__(self, name, health, attack, defend, hero=False):
        self.name = name
        self.defend = defend
        self.attack = attack
        self.health = health
        self.dressed = False
        self.hero = hero
        self.things_applied = []

    @property
    def health(self):
        return self._health

    @health.setter
    def health(self, health):
        if health > 0:
            self._health = health
            self.alive = True
        else:
            self._health = 0.0
            self.alive = False

    def _dress_up(self, thing: Things):
        self.defend += thing.defend * self.COEFFICIENTS['DEFEND_COEFFICIENT']
        self.attack += thing.attack * self.COEFFICIENTS['ATTACK_COEFFICIENT']
        self.health += thing.health * self.COEFFICIENTS['HEALTH_COEFFICIENT']
        self.things_applied.append(thing)
        if len(self.things_applied) == self.THINGS_NUM:
            self.dressed = True

    def _drop(self, thing: Things):
        self.defend -= thing.defend * self.COEFFICIENTS['DEFEND_COEFFICIENT']
        self.attack -= thing.attack * self.COEFFICIENTS['ATTACK_COEFFICIENT']
        self.health -= thing.health * self.COEFFICIENTS['HEALTH_COEFFICIENT']
        self.things_applied.pop(self.things_applied.index(thing))
        if len(self.things_applied) < self.THINGS_NUM:
            self.dressed = False

    def set_things(self, things):
        things_worn = []
        if self.dressed:
            # if there is already more things, than possible to wear
            return []
        if not isinstance(things, (list, tuple)):
            things = [things]
        for thing in things:
            if (thing.name not in [thing.name for thing in self.things_applied]
                    and not self.dressed):
                self._dress_up(thing)
                # pop this thing & store it in list of things_worn
                things_worn.append(things.pop(things.index(thing)))
        return things_worn

    def being_attacked(self, attack):
        self.health -= attack * self.defend

    def get_attack(self):
        return self.attack

    def drop_thing(self):
        if self.things_applied:
            thing = random.choice(self.things_applied)
            self._drop(thing)

    def __str__(self):
        response = f'{self.name}'
        return response if not self.hero else '(HERO) ' + response


class Paladin(Person):
    def __init__(self, name, health, attack, defend):
        self.COEFFICIENTS['DEFEND_COEFFICIENT'] = 2
        self.COEFFICIENTS['HEALTH_COEFFICIENT'] = 2
        super().__init__(name,
                         health * self.COEFFICIENTS['HEALTH_COEFFICIENT'],
                         attack,
                         defend * self.COEFFICIENTS['DEFEND_COEFFICIENT'])


class Warrior(Person):
    def __init__(self, name, health, attack, defend):
        self.COEFFICIENTS['ATTACK_COEFFICIENT'] = 2
        super().__init__(name, health,
                         attack * self.COEFFICIENTS['ATTACK_COEFFICIENT'],
                         defend)


class Orc(Person):
    POWER = 1.2
    PARAMS_NUM = 4

    def __init__(self, name, health, attack, defend, power):
        self.COEFFICIENTS['ATTACK_COEFFICIENT'] = 4
        self.power = power
        super().__init__(name, health,
                         attack * self.COEFFICIENTS['ATTACK_COEFFICIENT'],
                         defend)

    def get_attack(self):
        return self.attack * self.POWER


class Elf(Person):
    DODGE = 0.5
    PARAMS_NUM = 4

    def __init__(self, name, health, attack, defend, speed):
        self.COEFFICIENTS['ATTACK_COEFFICIENT'] = 0.5
        self.COEFFICIENTS['DEFEND_COEFFICIENT'] = 5
        self.COEFFICIENTS['HEALTH_COEFFICIENT'] = 1.5
        self.speed = speed
        super().__init__(name,
                         health * self.COEFFICIENTS['HEALTH_COEFFICIENT'],
                         attack * self.COEFFICIENTS['ATTACK_COEFFICIENT'],
                         defend * self.COEFFICIENTS['DEFEND_COEFFICIENT'])

    def being_attacked(self, attack):
        self.health -= max(attack * self.defend - self.speed * self.DODGE, 0)


class Mag(Person):
    MAGIC_DEFENCE = 0.5
    PARAMS_NUM = 4

    def __init__(self, name, health, attack, defend, magic):
        self.COEFFICIENTS['ATTACK_COEFFICIENT'] = 3
        self.COEFFICIENTS['DEFEND_COEFFICIENT'] = 3
        self.COEFFICIENTS['HEALTH_COEFFICIENT'] = 3
        self.magic = magic
        super().__init__(name,
                         health * self.COEFFICIENTS['HEALTH_COEFFICIENT'],
                         attack * self.COEFFICIENTS['ATTACK_COEFFICIENT'],
                         defend * self.COEFFICIENTS['DEFEND_COEFFICIENT'])

    def being_attacked(self, attack):
        self.health -= attack * self.defend - self.magic * self.MAGIC_DEFENCE


def single_fight(attacker, defender):
    """
    Single step of a game. Before the round there's a dice roll,
    when True is returned then attacker drop random thing.
    :param attacker: Person is about to attack.
    :param defender: Person is about to defend.
    :return: str result of a round.
    """
    if attacker.health <= 0:
        return TEXT['dead'].format(
            name=attacker, player_type=attacker.__class__.__name__)
    defender_health_bef = defender.health
    defender.being_attacked(attacker.get_attack())
    return TEXT['attack'].format(
        attacker_name=attacker,
        attacker_class=attacker.__class__.__name__,
        defender_name=defender.name,
        defender_class=defender.__class__.__name__,
        attacker_attack=round_wrapper(attacker.attack),
        defender_health_bef=round_wrapper(defender_health_bef),
        defender_health_aft=round_wrapper(defender.health)
    )


def fight(characters):
    """
    While there is > 1 player on a ring repeats single_fight.
    :param characters: All persons who take part in the fight.
    :return: None, rather prints to stdout the winner.
    """
    while len(characters) > 1:
        attacker, defender = random.sample(characters, 2)
        if roll_dice:
            attacker.drop_thing()
        score = single_fight(attacker, defender)
        print(score)
        if not defender.alive:
            dead = characters.pop(characters.index(defender))
            print(TEXT['dead'].format(
                name=dead, player_type=dead.__class__.__name__))
    winner = characters[-1]
    print(TEXT['winner'].format(
        name=winner, health=round_wrapper(winner.health),
        winner_type=winner.__class__.__name__))


def get_things(things=None):
    """
    Generate some things of type Things and sort them out acc. to defend key.
    :param things: list of Things.
    :return: sorted list of things.
    """
    if things is None:
        things = [
            Things('Ring', 0.01, 0, 0),
            Things('Sworn', 0, 0.6, 0),
            Things('Dark Sworn', 0, 0.2, 0),
            Things('Devil\'s Sworn', 0, 0.55, 0),
            Things('Elf\'s Gloves', 1, 0, 0),
            Things('Elf\'s Gloves', 1, 0, 0),
            Things('Elf\'s Boots', 0.1, 0, 0.5),
            Things('Ogr\'s Gloves', 0.00, 0.05, 0),
            Things('Dragon Armor', 0.1, 0, 0.5),
            Things('Goblin Armor', 0.15, 0, 0.2),
        ]
    return sorted(things, key=lambda t: t.defend)


def get_players(num):
    """
    Randomly creates list of further persons, i.e. players=fighters.
    :param num: int how many fighters should be generated.
    :return: list of Persons of len num.
    """
    def rnd(scale=0.2, times=3):
        return [random.random() / (1 / scale) for _ in range(times)]

    names = ['Jamison', 'Hunter', 'Lucian', 'Malaki', 'Hamza', 'Talon',
             'Tyshawn', 'Jaylen', 'Jadyn', 'Theodore', 'Braylen',
             'Jayvion', 'Branson', 'Colten', 'Ryker', 'Andre', 'Cael',
             'Osvaldo', 'Ari', 'Brycen']
    characters = []
    for _ in range(num):
        cls = random.choice(list(CHARACTER_SET))
        characters.append(
            cls(random.choice(names), *rnd(times=cls.PARAMS_NUM)))
    return characters


def create_own_player():
    """
    Generates a hero pf Person type.
    :return: Person.
    """
    if args.kind in CHARACTER_DATA:
        props = CHARACTER_DATA[args.kind]
        character = props[0](*props[1:])
        character.hero = True
        return character
    print(TEXT['error_player_not_found'].format(kind=args.kind))
    pl = Paladin('Rob', 1.2, 0.4, 2.5)
    pl.hero = True
    return pl


def prepare_fight(things=None, characters=None):
    # step 1: generate list of things & sort them inplace.
    if things is None:
        things = get_things()

    # step 2: randomly generate characters.
    if characters is None:
        characters = get_players(PLAYERS_NUM)

    # create own player
    hero = create_own_player()
    characters.append(hero)

    # step 3: dress up the characters.
    characters_dressed = characters.copy()
    i = 0
    while (things and
           not all([character.dressed for character in characters_dressed])
           and i <= 1000):
        character = random.choice(characters_dressed)
        things_rnd = random.sample(things, (random.randint(1, len(things))))
        things_worn = character.set_things(things_rnd)
        for worn in things_worn:
            things.pop(things.index(worn))
        if character.dressed:
            characters_dressed.pop(characters_dressed.index(character))
        i += 1
    return characters


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('--name', type=str, default='Hero',
                        required=False)
    parser.add_argument('--kind', type=str, default='Paladin', required=False)
    parser.add_argument('--health', type=float, default=1, required=False)
    parser.add_argument('--attack', type=float, default=1, required=False)
    parser.add_argument('--defend', type=float, default=1, required=False)
    parser.add_argument('--speed', type=float, default=1, required=False)
    parser.add_argument('--power', type=float, default=1, required=False)
    parser.add_argument('--magic', type=float, default=1, required=False)

    parser.add_argument('--players', type=int, default=2, required=False)
    return parser.parse_args()


if __name__ == '__main__':
    # Example how to run it
    # python game.py --name HERO --kind
    # Elf --healt 10 --attack 10 --defend 10 --speed 10
    args = parse_args()
    PLAYERS_NUM = args.players
    CHARACTER_DATA = {
        'Paladin': (Paladin, args.name, args.health, args.attack, args.defend),
        'Warrior': (Warrior, args.name, args.health, args.attack, args.defend),
        'Elf': (Elf, args.name, args.health,
                args.attack, args.defend, args.speed),
        'Orc': (Elf, args.name, args.health,
                args.attack, args.defend, args.power),
        'Mag': (Elf, args.name, args.health,
                args.attack, args.defend, args.magic)}
    CHARACTER_SET = [ch[0] for ch in CHARACTER_DATA.values()]
    # generate things & characters
    fighters = prepare_fight()
    # start fight
    fight(fighters)
