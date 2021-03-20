from random import randrange, shuffle, sample

class Thing:
    def __init__(self, name, protection, attack, life):
        # protection - %, attack - number, life - number
        self.name = name
        self.protection = protection
        self.attack = attack
        self.life = life

class Person:
    def __init__(self, name, protection, attack, life):
        self.name = name
        self.protection = protection
        self.attack = attack
        self.life = life

    def setThings(self, things):
        if len(things) == 0:
            1 == 1
        else:
            #опряделяем рандомное кол-во вещей с ограничениями в условии, кот-ое будем надевать. Да, 0 тоже может быть
            number_things = randrange(5)
            if number_things > len(things):
                number_things = len(things)
            #теперь выбираем рандомные вещи из списка вещей
            for i in range(number_things):
                thing = things.pop(randrange(len(things)))
                self.protection = self.protection + thing.protection
                self.attack = self.attack + thing.attack
                self.life = self.life + thing.life
            #protection не может быть > 1
            if self.protection >= 1:
                self.protection = 0.99

    def decrease_life(self, attack_damage):
        damage = attack_damage - attack_damage*self.protection
        self.life = self.life - damage

class Paladin(Person):
    def __init__(self, name, protection, attack, life):
        super().__init__(name, protection, attack, life)
        self.protection = self.protection * 2
        if self.protection >= 1:
            self.protection = 0.99
        self.life = self.life * 2

class Warrior(Person):
    def __init__(self, name, protection, attack, life):
        super().__init__(name, protection, attack, life)
        self.attack = self.attack * 2
        if self.protection >= 1:
            self.protection = 0.99

#Шаг 1. Создаем произвольное кол-во вещей
power_ring = Thing('power_ring', 0.01, 10,0)
bubble_life = Thing('bubble_life', 0.02, 0, 20)
security_crown = Thing('security_crown', 0.02, 0, 20)
pussy_glove = Thing('pussy_glove', 0, 3, 0)
animal_armor = Thing('animal_armor', 0.05, 5, 15)
useless_thing = Thing('useless_thing', 0, 1, 1)
god_mode = Thing('god_mode', 0.1, 20, 20)

things = sorted([power_ring, bubble_life, security_crown,
          pussy_glove, animal_armor, useless_thing, god_mode], key=lambda x: x.protection)

names_list = ['jordan', 'pitt', 'jolie', 'james', 'anaconda', 'tiger', 'leon', 'watson', 'putin', 'obama',
              'filippova', 'lukin', 'catwoman', 'baygarin', 'tsvigun', 'l jackson', 'pepe', 'messe', 'ronaldu', 'batman']

#Шаг 2. Создаем рандомных персонажей
hero_1 = Paladin(names_list.pop(randrange(len(names_list))), 0.5, 20, 80)
hero_2 = Paladin(names_list.pop(randrange(len(names_list))), 0.1, 10, 30)
hero_3 = Paladin(names_list.pop(randrange(len(names_list))), 0.7, 20, 50)
hero_4 = Paladin(names_list.pop(randrange(len(names_list))), 0.8, 60, 90)
hero_5 = Paladin(names_list.pop(randrange(len(names_list))), 0.3, 40, 60)
hero_6 = Warrior(names_list.pop(randrange(len(names_list))), 0.1, 80, 50)
hero_7 = Warrior(names_list.pop(randrange(len(names_list))), 0.4, 60, 30)
hero_8 = Warrior(names_list.pop(randrange(len(names_list))), 0.3, 40, 10)
hero_9 = Warrior(names_list.pop(randrange(len(names_list))), 0.7, 30, 80)
hero_10 = Warrior(names_list.pop(randrange(len(names_list))), 0.9, 80, 90)

heroes = [hero_1, hero_2, hero_3, hero_4, hero_5, hero_6, hero_7, hero_8, hero_9, hero_10]

#Перемешаю списко heroes, чтобы герои в конце не получила всегда нулевые очки, т.к. вещи получают не все герои
shuffle(heroes)

#Шаг 3. Одеваем персонажей рандомными вещами
for hero in (heroes):
        hero.setThings(things)

#Шаг 4.
while len(heroes) > 1:
    #выбираю рандомно пару игроков для схватки
    players = sample(heroes, 2)
    attacking = players[0]
    defensing = players[1]

    print(f'{attacking.name} наносит удар по {defensing.name} на {attacking.attack} урона')
    defensing.decrease_life(attacking.attack)

    if defensing.life <= 0:
        heroes.remove(defensing)

print(f'Победитель сражения - {heroes[0].name}')



