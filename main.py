import random


class Thing:
    """Шмотки всякие разные"""
    def __init__(self, name, defence, attack, health):
        self.name = name
        self.defence = defence
        self.attack = attack
        self.health = health


class Person:
    """Основа для персонажа"""
    def __init__(self, name, defence, attack, health):
        self.name = name
        self.defence = defence * 0.01
        self.attack = attack
        self.health = health

    things = []

    def setThings(self, things):
        self.things = things
        for thing in things:
            self.attack += thing.attack
            self.defence += thing.defence * 0.01
            self.health += thing.health

    def take_damage(self, attack_damage):
        damage = attack_damage - attack_damage * self.defence
        self.health = self.health - damage
        return damage

    """еще нужны методы для выполнения какого-то там алгоритма"""


class Paladin(Person):
    def __init__(self, name, defence, attack, health):
        self.name = name
        self.defence = defence * 2 * 0.01
        self.attack = attack
        self.health = health
    class_name = "Паладин"


class Warrior(Person):
    def __init__(self, name, defence, attack, health):
        self.name = name
        self.defence = defence * 0.01
        self.attack = attack * 2
        self.health = health
    class_name = "Воин"


class Game():
    HELMETS = [
        "Кожаный шлем",
        "Медный шлем",
        "Железный шлем",
        "Серебряный шлем",
        "Горящая шапка вора",
        "Ковбойская шляпа",
        "Зачарованный венок",
        "Парик из волос убитых врагов",
        "Шапка из фольги",
        "Грибной шлем",
        "Шлем из арбуза"
    ]
    ARMORS = [
        "Кожаная броня",
        "Медная броня",
        "Железная броня",
        "Серебрянная броня",
        "Жилет Вассермана",
        "Бронелифчик",
        "Рваная рубаха",
        "Королевское одеяние",
        "Умная куртка с Wi-Fi и Bluetooth",
        "Королевский нагрудник Зены"
    ]
    LEGS = [
        "Кожаные штаны",
        "Медные штаны",
        "Железные штаны",
        "Серебрянные штаны",
        "Пляжные шорты",
        "Штаны с подворотами",
        "Джинсы от Armani",
        "Спортивные штаны Abibas",
        "Кальсоны с подогревом"
    ]
    GLOVES = [
        "Кожаные перчатки",
        "Медные перчатки",
        "Железные перчатки",
        "Серебрянные перчатки",
        "Тактические перчатки",
        "Хирургические перчатки",
        "Королевские перчатки",
        "Варежки",
        "Рокерские перчатки",
        "Наручники Гали Гадот"
    ]
    WEAPONS = [
        "Деревянный меч",
        "Медный меч",
        "Железный меч",
        "Серебрянный меч",
        "Кастеты",
        "Железная булава",
        "Скалка",
        "Бита",
        "Кинжал",
        "Кириллическое кадило патриарха"
    ]
    NAMES = [
        "Жора Пакетик",
        "Николай Сгущёнка",
        "Сеня Водолаз",
        "Валя Стакан",
        "Володя Ржавый",
        "Терентий Ловелас",
        "Леха Волчара",
        "Толян Торпеда",
        "Андрюха Хлыст",
        "Гоша Паштет",
        "Саня Горностай",
        "Альберт Импортный",
        "Володарчик Таксист",
        "Серега Спартаковский",
        "Кама Пуля",
        "Сава Майонез",
        "Александр Борода",
        "Лёня Раздолбай",
        "Костян Седой",
        "Дима Мозг"
    ]
    NUMBER_OF_PERSONS = 10

    def create_items(self, counter):
        all_items = [
            self.HELMETS,
            self.ARMORS,
            self.LEGS,
            self.GLOVES,
            self.WEAPONS
        ]
        items = []
        for i in range(counter):
            item_type = random.choice(all_items)
            name = random.choice(item_type)
            item_type.remove(name)
            defence = random.randint(0, 10)
            attack = random.randint(5, 30)
            health = random.randint(10, 100)
            new_item = Thing(name, defence, attack, health)
            items.append(new_item)
        print(f"Сегодня на арене {counter} предметов.")
        # Сортируем список предметов
        defence_points = []
        for item in items:
            defence_points.append(item.defence)
        defence_points_sorted = sorted(defence_points)
        sorted_items = []
        while len(items) > 0:
            for item in items:
                if item.defence == defence_points_sorted[-1]:
                    sorted_items.append(item)
                    items.remove(item)
                    defence_points_sorted.pop()
                else:
                    continue
        return sorted_items

    def create_persons(self):
        classes = ["paladin", "warrior"]
        persons = []
        for i in range(self.NUMBER_OF_PERSONS):
            name = random.choice(self.NAMES)
            self.NAMES.remove(name)
            defence = random.randint(0, 15)
            attack = random.randint(5, 15)
            health = random.randint(10, 30)
            person_class = random.choice(classes)
            if person_class == "paladin":
                new_person = Paladin(name, defence, attack, health)
            else:
                new_person = Warrior(name, defence, attack, health)
            persons.append(new_person)
        return persons

    def start_new_game(self):
        print("Добро пожаловать на пивную арену!")
        # 1 шаг - создаем предметы
        items = self.create_items(random.randint(10, 30))

        # 2 шаг - создаем персонажей
        persons = self.create_persons()
        print("Герои сегодняшнего дня:")
        for person in persons:
            print(f'{person.class_name} - {person.name}')

        # 3 шаг - одеваем персонажей
        print("Даем героям предметы:")
        print('-----------')
        for person in persons:
            number_of_items = random.randint(0, 4)
            things = []
            if number_of_items > len(items):
                number_of_items = len(items)
            if number_of_items > 0:
                for i in range(0, number_of_items):
                    item = random.choice(items)
                    things.append(item)
                    items.remove(item)
                person.setThings(things)
                print(f'{person.name} получает:')
                for thing in person.things:
                    print(thing.name)
            else:
                print(f'{person.name} не получает ничего!')
            print('-----------')

        # Шаг 4 - Начинаем бой!
        print('Да начнется битва!')
        while len(persons) > 1:
            attack_person = random.choice(persons)
            defending_person = random.choice(persons)
            if attack_person == defending_person:
                continue
            damage = round(defending_person.take_damage(attack_person.attack), 2)
            print(f'{attack_person.name} наносит удар по {defending_person.name}'
                  f' на {damage} урона')
            if defending_person.health <= 0:
                persons.remove(defending_person)
                print(f'{defending_person.name} погиб!')
        print(f'{person.class_name} {persons[0].name} победил! Кто-нибудь, налейте ему пива!')


new_game = Game()
new_game.start_new_game()
