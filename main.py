
class Thing:
    ZERO_CASE = 'Параметр {parameter} не указан, поэтому установлено значение 0'
    LIMIT_CASE = ('Защита не может быть больше {limit}%. Для {name} установлена'
                  ' максимальная защита')
    PARAMETER = {'hp':'здоровья', 'dp':'защиты', 'ap':'атаки'}
    MAX_DEFENSE = 5

    def __init__(self, name, health=None, defense=None, attack=None):
        self.thing_name = name
        self.added_health = self.have_parameter(self.PARAMETER['hp'], health)
        self.added_defense = self.have_parameter(self.PARAMETER['dp'],
                                                 defense,self.MAX_DEFENSE,
                                                 name)
        self.added_attack = self.have_parameter(self.PARAMETER['ap'], attack)

    def have_parameter(self, parameter, value=None, limit=None, name=None):
        if value is None:
            print(self.ZERO_CASE.format(parameter=parameter))
            return 0
        elif limit is not None:
            if value >= limit:
                print(self.LIMIT_CASE.format(limit=limit, name=name))
                return limit
        return value



class Person():
    INVENTORY = []
    MAX_DEFENSE = 30

    def __init__(self, name, health, defense, attack):
        self.person_name = name
        self.base_health = health
        self.base_defense = self.have_defense(defense)
        self.base_attack = attack

    def have_defense(self, defense):
        return self.DEFENSE_LIMIT if defense >= self.DEFENSE_LIMIT else defense

    def set_things(self, things):
        pass

    def take_damage(self, ):
        pass

    def attack_damage(self, ):
        pass


class Paladind(Person):

    def __init__(self, health, defense):
        self.health = health * 2
        self.defense = self.have_defense(defense)


class Warrior(Person):

    def __init__(self, attack):
        self.attack = attack * 2


class Wizard(Person):

    def __init__(self, health, defense, attack):
        self.health = health / 2
        self.defense =  self.have_defense(defense) / 2
        self.attack = attack * 4


if __name__ == '__main__':
    ring_of_power = Thing(name="Кольцо Всевластия", health=-5, defense=100)
