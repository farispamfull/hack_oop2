import random

NICK_NAMES = ['Grom', 'Trum', 'Drog', 'Karg', 'Gorrum', 'Igrim', 'Dragga',
              'Hargu', 'Agra', 'Grimma',
              'Arthas', 'Tirion', 'Lady Liadrin', 'Turalion',
              'Uther', 'Bolvar',
              'Aleksandros', 'Granis', 'Arius', 'Mallak']

# присвоение рандомного имени


def set_name():
    nick_name = random.choice(NICK_NAMES)
    NICK_NAMES.remove(nick_name)
    return nick_name


class Thing:

    def __init__(self, name, armour, attack, health):
        self.name = name
        self.armour = armour * 0.01
        self.attack = attack
        self.health = health

# создание персонажа


class Person():
    HEROES = []

    def __init__(self, name='Player', health_points=500,
                 based_attack=100, based_armour=1):
        self.name = name
        self.health_points = health_points
        self.based_attack = based_attack
        self.based_armour = based_armour * 0.01
        self.items = []
    # присвоение предмета персонажу и добавление предмета в список предметов

    def set_things(self, thing):
        self.items.append(thing)
    # присвоение персонажу рандомные характеристики

    def create_hero(self):
        self.name = set_name()
        self.health_points = random.randint(500, 1001)
        self.based_attack = random.randint(50, 101)
        self.based_armour = random.randint(0, 11) * 0.01

    def attack_damage(self):
        items_damage = sum(item.attack for item in self.items)
        return self.based_attack + items_damage

    def final_protect(self):
        item_armour = sum(item.armour for item in self.items)
        return self.based_armour + item_armour

    def fight(self, person):
        attacker_damage = self.attack_damage()
        damage = (attacker_damage -
                  attacker_damage * person.final_protect())
        person.health_points -= damage
        if person.health_points <= 0:
            Person.HEROES.remove(person)
        return round(damage, 2)
# создание героя паладина


class Paladin(Person):

    def __init__(self, name='Player', health_points=500,
                 based_attack=50, based_armour=1):
        super().__init__(name, based_attack)
        self.health_points = health_points * 2
        self.based_armour = based_armour * 0.01 * 2

    def create_hero(self):
        self.name = set_name()
        self.health_points = random.randint(500, 1001) * 2
        self.based_attack = random.randint(50, 101)
        self.based_armour = random.randint(0, 11) * 0.01 * 2

# создание героя война


class Warrior(Person):

    def __init__(self, name='Player', health_points=500,
                 based_attack=50, based_armour=1):
        super().__init__(name, health_points, based_armour)
        self.based_attack = based_attack * 2

    def create_hero(self):
        self.name = set_name()
        self.health_points = random.randint(500, 1001)
        self.based_attack = random.randint(101, 150) * 2
        self.based_armour = random.randint(0, 11) * 0.01

# создание всех предметов


def create_items():
    return {
        'shield': Thing('shield', 10, 15, 250),
        'chest_armour': Thing('chest armour', 9, 10, 200),
        'helmet': Thing('helmet', 8, 10, 125),
        'shoes': Thing('shoes', 7, 15, 150),
        'armbands': Thing('armbands', 5, 15, 75),
        'belt': Thing('belt', 3, 5, 100),
        'rings': Thing('rings', 2, 5, 150),
        'amulet': Thing('amulet', 1, 7, 125),
        'weapon': Thing('weapon', 0, 50, 100)
    }


def main():
    # создание всех героев
    def create_heroes():
        paladins_number = random.randint(0, 11)
        paladins = [Paladin() for i in range(paladins_number)]
        for paladin in paladins:
            paladin.create_hero()
            Person.HEROES.append(paladin)
        warriors_number = 10 - paladins_number
        warriors = [Warrior() for i in range(warriors_number)]
        for warrior in warriors:
            warrior.create_hero()
            Person.HEROES.append(warrior)

        # присвоение каждому герою определенное количество вещей

    def set_items():
        for hero in Person.HEROES:
            items_amount = random.randint(1, 5)
            taken_items = []
            for i in range(items_amount):
                item = random.choice(list(create_items().keys()))
                if item not in taken_items:
                    hero.set_things(create_items()[item])
                    taken_items.append(item)
                else:
                    items_amount += 1

    def arena():
        while len(Person.HEROES) != 1:
            attacker = random.choice(Person.HEROES)
            fighters = [hero for hero in Person.HEROES
                        if hero.name != attacker.name]
            defender = random.choice(fighters)
            print(f'{attacker.name} наносит удар по '
                  f'{defender.name} на {attacker.fight(defender)} урона')

    create_heroes()
    set_items()
    arena()
    print(f'Победитель - {Person.HEROES[0].name}')


main()
