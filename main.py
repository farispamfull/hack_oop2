



class Thing:

    def __init__(self, name, health=None, defense=None, attack=None):
        self.thing_name = name 
        self.added_health = 0 if health is None else health
        self.added_defense = 0 if defense is None else defense
        self.added_attack = 0 if attack is None else attack


class Person():

    def __init__(self, name, health, defense, attack):
        self.person_name = name
        self.base_health = health
        self.base_defense = 30 if defense >= 30 else defense
        self.base_attack = attack

    def set_things(things):
        pass

    def take_damage():
        pass
        
    def make_damage():
        pass


class Paladind(Person):

    def __init__(self, health, defense):
        self.health = health * 2
        self.defense = defense * 2


class Warrior(Person):

    def __init__(self, attack):
        self.attack = attack * 2


class Wizard(Person):

    def __init__(self, health, defense, attack):
        self.health = health / 2
        self.defense = defense / 2
        self.attack = attack * 4


if __name__ == '__main__':

