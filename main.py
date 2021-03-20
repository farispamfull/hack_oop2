import random


class Thing:
    MAX_RATE = 10
    MIN_HP = 5
    MAX_HP = 30

    def __init__(self):
        self.name = 'Magic Thing'
        self.attack = random.randint(0, self.MAX_RATE)
        self.defence = random.randint(0, self.MAX_RATE)
        self.hp = random.randint(self.MIN_HP, self.MAX_HP)

    def __str__(self):
        return (f'{self.name:20} Attack: {self.attack:<10} '
                f'Defence: {self.defence:<10} HP: {self.hp:3}')


class Person:
    MAX_DEFENCE = 70  # Total maximum defence with things

    def __init__(self, name, base_attack, base_defence, base_hp):
        self.name = name
        self.base_attack = base_attack
        self.base_defence = base_defence
        self.base_hp = base_hp
        self.things = []

        # Resulting characteristics with things
        self.attack = self.base_attack
        self.defence = self.base_defence
        self.hp = self.base_hp

    def set_things(self, thing):
        self.things.append(thing)
        for thing in self.things:
            self.attack += self.attack * thing.attack / 100
            self.defence += thing.defence
            #
            if self.defence > self.MAX_DEFENCE:
                self.defence = self.MAX_DEFENCE
            self.hp += thing.hp

    def reduce_hp(self, attack_damage):
        damage = attack_damage * (100 - self.defence) / 100
        self.hp = self.hp - damage
        return damage

    def __str__(self):
        return (f'{self.name:20} Attack: {self.base_attack:<10} '
                f'Defence: {self.base_defence:<10} HP: {self.hp}')


class Paladin(Person):
    def __init__(self, name, base_attack, base_defence, base_hp):
        super().__init__(name, base_attack, base_defence, base_hp)
        self.base_defence = base_defence * 2
        self.base_hp = base_hp * 2


class Warrior(Person):
    def __init__(self, name, base_attack, base_defence, base_hp):
        super().__init__(name, base_attack, base_defence, base_hp)
        self.base_attack = base_attack * 2


class Arena:
    things = []
    fighters = []

    def generate_things(self, number):
        for item in range(number):
            self.things.append(Thing())

    def generate_fighters(self, number):
        BASE_ATTACK = 30
        BASE_DEFENCE = 20
        BASE_HP = 100

        names = [
            'Connor MacLeod',
            'Duncan MacLeod',
            'Alan Wake',
            'Trump',
            'Nikolay Valuev',
            'Vasiliy Chapayev',
            'Mike Smith',
            'David Backham',
            'Alan Po',
            'Ma Hongyu',
            'David Chase',
            'Silvio Dante',
            'Walter White',
            ''
        ]
        for i in range(number):
            # Randomly choose name and delete it from list to avoid name duplication
            name_point = random.randrange(0, len(names))
            name = names.pop(name_point)
            person_type = random.randint(0, 1)
            attack = random.randint(BASE_ATTACK//2, BASE_ATTACK)
            defence = random.randint(BASE_DEFENCE // 2, BASE_DEFENCE)
            hp = random.randint(BASE_HP // 2, BASE_HP)
            if person_type == 0:
                fighter = Paladin(name, base_attack=attack, base_defence=defence, base_hp=hp)
            else:
                fighter = Warrior(name, base_attack=attack, base_defence=defence, base_hp=hp)
            self.fighters.append(fighter)

    def give_things(self):
        # Things are given to fighters in ROUND-ROBIN order
        order = 0
        for thing in self.things:
            self.fighters[order % 10].set_things(thing)
            order = order + 1

    def fight(self):
        fighters_left = len(self.fighters)
        while fighters_left > 1:
            fighters_number = list(range(fighters_left))
            attacking = fighters_number.pop(random.randrange(0, fighters_left))
            defending = fighters_number[random.randrange(0, fighters_left - 1)]
            damage = self.fighters[defending].reduce_hp(self.fighters[attacking].attack)
            print(f'{self.fighters[attacking].name:20} наносит удар по '
                  f'{self.fighters[defending].name:20} на {damage:.4} урона')
            if self.fighters[defending].hp <= 0:
                print(f'{self.fighters[defending].name} destroyed!')
                self.fighters.pop(defending)
                fighters_left = len(self.fighters)
        print(f'The winner is {self.fighters[0].name}')


if __name__ == '__main__':
    FIGHTERS_NUMBER = 10
    THINGS_MAX_NUMBER = 4 * FIGHTERS_NUMBER  # up to 4 things for each fighter

    arena = Arena()
    things_number = random.randint(10, THINGS_MAX_NUMBER)
    arena.generate_things(things_number)
    arena.generate_fighters(FIGHTERS_NUMBER)
    arena.give_things()
    print('There can be the only one!\n')
    arena.fight()
