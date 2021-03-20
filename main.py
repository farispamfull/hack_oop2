
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
    DEATH_PERSON = 'Что мертво, умереть не может. Персонаж {name} уже мёртв'
    INVENTORY = []
    MAX_DEFENSE = 30
    LIMIT_CASE = ('Защита не может быть больше {limit}%. У {name} максимальная'
                  ' защита')

    def __init__(self, name, health, defense, attack):
        if health <= 0:
            print(self.DEATH_PERSON.format(name=name))
        self.person_name = name
        self.base_health = health
        self.base_defense = self.have_defense(defense, name)
        self.base_attack = attack

    def have_defense(self, parameter, name):
        limit = self.MAX_DEFENSE
        if parameter >= limit:
            print(self.LIMIT_CASE.format(limit=limit,name=name))
            return limit
        return parameter

    def set_things(self, things):
        self.INVENTORY.append(things)

    def take_damage(self, ):
        pass

    def attack_damage(self, ):
        pass


class Paladind(Person):

    def __init__(self, name, health, defense, attack):
        super(Paladind, self).__init__(name, health, defense, attack)
        self.base_health *= 2
        self.base_defense *= 2


class Warrior(Person):

    def __init__(self, name, health, defense, attack):
        super(Warrior, self).__init__(name, health, defense, attack)
        self.base_attack *= 2


class Wizard(Person):

    def __init__(self, name, health, defense, attack):
        super(Wizard, self).__init__(name, health, defense, attack)
        if self.base_health > 0:
            self.base_health /= 3
        self.base_attack *= 3


if __name__ == '__main__':
    ring_of_power = Thing(name="Кольцо Всевластия", health=-5, defense=100)
    superman = Person('Супермэн', 1000, 100, 100)
    zombie = Wizard('Зомби', 0, 0, 30)
    
    print(zombie.person_name, zombie.base_health, zombie.base_defense, zombie.base_attack)
