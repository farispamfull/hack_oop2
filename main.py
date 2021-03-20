import colorama
from colorama import Fore, Style
import random
import time

# База имен
NAMES_DB = [
    'Логроут',
    'Фанохт',
    'Мугморсок',
    'Ротгротунк',
    'Руталаг',
    'Хоркархт',
    'Кромортук',
    'Рунлилод',
    'Мокутокк',
    'Моккаглаз',
    'Хелренокк',
    'Волтарнал',
    'Кернкачет',
    'Йелколач',
    'Нерфизен',
    'Донтливар',
    'Саригрум',
    'Крагнадор',
    'Крогливоч',
    'Роггрофан',
]

# База генерируемых прозвищ:
SUBNAME_DB = [
    ['Кровавый', 'Орел'],
    ['Яростный', 'Клык'],
    ['Неистовый', 'Череп'],
    ['Дикий', 'Рок'],
    ['Безумный', 'Рык'],
    ['Жестокий', 'Кулак']
]

# База предметов:
THINGS_DB = {
    'Оскверненный Доспех Боли': [90, 8, -0.23],
    'Клинок ослепляющей Ярости': [-40, 60, -0.1],
    'Меч Проклятых душ': [0, 26, -0.05],
    'Топор Войны': [0, 13, 0],
    'Ржавый тесак Мясника': [0, 5, 0],
    'Щит бедняка': [0, 2, 0.03],
    'Старая кольчуга': [10, 0, 0.04],
    'Кольцо Лунного света': [15, 8, 0.07],
    'Доспехи стражника Зигкурата': [23, 0, 0.08],
    'Туника магической защиты': [0, 0, 0.1],
}

units = []


class Person:

    def __init__(self):
        self.name = self.name_gen()
        self.base_hp = 100
        self.base_attack = 15
        self.base_defence = 0.1
        self.things = []

    def name_gen(self):
        name_bd_len = len(NAMES_DB) - 1
        subname_bd_len = len(SUBNAME_DB) - 1
        rand_name = NAMES_DB[random.randint(1, name_bd_len)]
        rand_subname = str(SUBNAME_DB[random.randint(0, subname_bd_len)][0])
        rand_subname2 = str(SUBNAME_DB[random.randint(0, subname_bd_len)][1])
        name = f'{rand_name} "{rand_subname} {rand_subname2}"'
        return name

    def setThings(self):
        for _ in range(random.randint(0, 4)):
            things_list = list(THINGS_DB.keys())
            name = random.choice(things_list)
            self.things.append(Thing(name))
        self.final_params()

    def final_params(self):
        self.final_hp = self.base_hp
        self.final_attack = self.base_attack
        self.final_defence = self.base_defence
        for i in range(len(self.things)):
            self.final_hp += self.things[i].health
            self.final_attack += self.things[i].attack
            self.final_defence += self.things[i].defence


class Thing:
    def __init__(self, name):
        self.name = name
        self.defence = THINGS_DB[name][2]
        self.attack = THINGS_DB[name][1]
        self.health = THINGS_DB[name][0]


class Warrior(Person):
    def __init__(self):
        super().__init__()
        self.base_attack = 2 * self.base_attack
        self.class_name = 'Воин'


class Paladin(Person):
    def __init__(self):
        super().__init__()
        self.base_defence = 2 * self.base_defence
        self.base_hp = 2 * self.base_hp
        self.class_name = 'Паладин'


class Elf(Person):
    def __init__(self):
        super().__init__()
        self.base_attack = 1.5 * self.base_attack
        self.base_defence = 1.25 * self.base_defence
        self.base_hp = 0.75 * self.base_hp
        self.class_name = 'Эльф'


# Функция битвы:
def battle():
    # Выбор двух бойцов:
    unit_1 = random.choice(units)
    unit_2 = random.choice(units)
    while True:
        # Проверка на совпадение имен:
        if unit_1.name != unit_2.name:
            # Обнуляем предметы перед каждой битвой:
            unit_1.things = []
            unit_2.things = []
            # Даем бойцам рандомные предметы:
            unit_1.setThings()
            for i in range(len(unit_1.things)):
                print(f'{unit_1.name} получил {unit_1.things[i].name}')
            unit_2.setThings()
            for i in range(len(unit_2.things)):
                print(f'{unit_2.name} получил {unit_2.things[i].name}')

            battle_units = [unit_1, unit_2]

            attacker = random.choice(battle_units)
            defencer = random.choice(battle_units)
            while True:
                # Проверка на совпадение имен:
                if attacker.name == defencer.name:
                    defencer = random.choice(battle_units)
                else:
                    defencer.final_hp -= (
                        attacker.final_attack * (1 - defencer.final_defence)
                    )
                    attack_value = round(
                        attacker.final_attack *
                        (1 - defencer.final_defence), 2)
                    print(f'{Fore.RED}{attacker.class_name}',
                          f'{attacker.name}{Style.RESET_ALL} наносит удар по',
                          f' {Fore.BLUE}{defencer.class_name}у ',
                          f'{defencer.name}{Style.RESET_ALL} на {Fore.RED}',
                          f'{attack_value}{Style.RESET_ALL} урона.')

                    print(f'{Fore.BLUE}{defencer.name}{Style.RESET_ALL} ',
                          f'Осталось HP:{Fore.GREEN}',
                          f'{round(defencer.final_hp, 2)}{Style.RESET_ALL}')
                    # Пауза между ударами для эпичности:
                    time.sleep(0.6)
                    if defencer.final_hp <= 0:
                        print(
                            f'{Fore.BLUE}{defencer.name}{Style.RESET_ALL}',
                            'был повержен!')
                        print(
                            f'Великий {Fore.RED}{attacker.name}',
                            f'{Style.RESET_ALL} победил!')
                        return defencer.name
                    # Рандомное переопределение атакующего
                    # и защищающегося на следуюший этап боя:
                    attacker = random.choice(battle_units)
                    defencer = random.choice(battle_units)
        else:
            unit_2 = random.choice(units)


# Генерация персонажей в список:
def create_units(num):
    unit_class = [Warrior, Paladin, Elf]
    for _ in range(num):
        unit = (random.choice(unit_class))()
        units.append(unit)
    print(f'{Fore.YELLOW}Перед Вами',
          f'{len(units)} Бойцов.{Style.RESET_ALL}')


# Королевская битва пока не останется последний выживший:
def battle_royal():
    while True:
        defeated = battle()
        for i in units:
            if i.name == defeated:
                units.remove(i)
                print(f'Осталось всего: {Fore.YELLOW}',
                      f'{len(units)} Бойцов.{Style.RESET_ALL}')
        if len(units) == 1:
            print(f'{Fore.YELLOW}{units[0].name}{Style.RESET_ALL}',
                  f' {Fore.RED}- Величайший Боец всех времен!!!',
                  f'{Style.RESET_ALL}')
            break


create_units(10)
battle_royal()
