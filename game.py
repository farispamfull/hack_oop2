import random
import logging

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(message)s', datefmt='%d-%b-%y %H:%M:%S')
logger = logging.getLogger(__name__)


LANGUAGE_WRAPPER = {
    'attack': ('{attacker_name} ({attacker_class}) '
               'с атакой в {attacker_attack} единиц '
               'наносит удар по '
               '{defender_name} ({defender_class} '
               'health={defender_health_bef}) '
               'на {attacker_attack} единиц урона. '
               'У {defender_name} остается {defender_health_aft} '
               'пунктов жизни.'),
    'dead': '{name} ({player_type}) был убит',
    'winner': '{name} ({winner_type}) побеждает со здоровьем в {health}!'
}
ROUND_RESULTS = 2


def round_wrapper(value, digits=ROUND_RESULTS):
    return int(value) if value == 0 else round(value, digits)


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
    # number of numeric params for further instances auto generation
    PARAMS_NUM = 3

    def __init__(self, name, health, attack, defend):
        self.name = name
        self.defend = defend
        self.attack = attack
        self.health = health
        self.dressed = False
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

    def __str__(self):
        return (f'{self.name} '
                f'({self.__class__.__name__}) '
                f'defend = {self.defend:.2f}, '
                f'attack = {self.attack:.2f}, '
                f'health = {self.health:.2f}, '
                f'is_alive = {self.alive}')

    def __repr__(self):
        return f'{self.name}'


class Paladin(Person):
    def __init__(self, name, health, attack, defend):
        """
        :param name: str name of Paladin
        :param health: health points
        :param attack: base attack points
        :param defend: ratio of defend points
        """
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
    defender_health_bef = defender.health
    defender.being_attacked(attacker.attack)
    return LANGUAGE_WRAPPER['attack'].format(
        attacker_name=attacker.name,
        attacker_class=attacker.__class__.__name__,
        defender_name=defender.name,
        defender_class=defender.__class__.__name__,
        attacker_attack=round_wrapper(attacker.attack),
        defender_health_bef=round_wrapper(defender_health_bef),
        defender_health_aft=round_wrapper(defender.health)
    )


def fight(characters):
    while len(characters) > 1:
        attacker, defender = random.sample(characters, 2)
        score = single_fight(attacker, defender)
        print(score)
        if not defender.alive:
            dead = characters.pop(characters.index(defender))
            print(LANGUAGE_WRAPPER['dead'].format(
                name=dead.name, player_type=dead.__class__.__name__))
    winner = characters[-1]
    print(LANGUAGE_WRAPPER['winner'].format(
        name=winner.name, health=round_wrapper(winner.health),
        winner_type=winner.__class__.__name__))


def prepare_fight(names=None, things=None, characters=None, characters_num=5):
    # step 1: generate list of things & sort them inplace.
    if things is None:
        things = [
            Things('Ring', 0.01, 0, 0),
            Things('Sworn', 0, 0.6, 0),
            Things('Elf\'s Gloves', 100, 0, 0),
            Things('Elf\'s Gloves', 100, 0, 0),
            Things('Ogr\'s Gloves', 0.00, 0.05, 0),
            Things('Dragon Armor', 0.1, 0, 0.5),
            Things('Goblin Armor', 0.15, 0, 0.2),
        ]
    things.sort(key=lambda t: t.defend)

    # print('------- Things sorted -------')
    # for thing in things:
    #     print(thing)

    # step 2: randomly generate characters.
    if characters is None:
        def rnd(scale=0.2, times=3):
            return [random.random() / (1 / scale) for _ in range(times)]
        if names is None:
            names = ['Jamison', 'Hunter', 'Lucian', 'Malaki', 'Hamza', 'Talon',
                     'Tyshawn', 'Jaylen', 'Jadyn', 'Theodore', 'Braylen',
                     'Jayvion', 'Branson', 'Colten', 'Ryker', 'Andre', 'Cael',
                     'Osvaldo', 'Ari', 'Brycen']
        characters = []
        for _ in range(characters_num):
            cls = random.choice(CHARACTERS_SET)
            characters.append(
                cls(random.choice(names), *rnd(times=cls.PARAMS_NUM)))

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

    # print('------- Characters -------')
    # for c in characters:
    #     print(c)
    # print('------- Characters -------')
    return characters


def test():
    pl = Warrior('Rob', 0.1, 2, 2)
    print(pl)


if __name__ == '__main__':
    CHARACTERS_SET = (Paladin, Warrior, Elf, Orc, Mag)
    # generate things & characters
    fighters = prepare_fight()
    # start fight
    fight(fighters)
