from typing import Optional, List, Any
from tkinter import *
from tkinter import scrolledtext
import random as rdm
import time

window_title = Tk()
window_title.title('Battle-arena')
window_title.geometry('850x400')
window_title["bg"]= "#FFCBBB"
title_list_sword_1 = Label(window_title, text="\n\n\nס₪₪₪₪§|(Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ>\n", 
                   font="Roboto 15", fg="Red", bg="#FFCBBB").grid(column=0, row=0)
title_list = Label(window_title, text="    Добро Пожаловать в игру Battle-arena, храбрый воин.\n "
                                "    В этом мире нет справедливости, но\n"
                                "    только самый умелый и достойный воин готов сразиться за нее.\n"
                                "    Если ты готов сражаться, то бери же свой могущественный меч!",
                                font="Roboto", fg="Black", bg="#FFCBBB").grid(column=0, row=5)
def click_clear():
    window_title.destroy()
btn_1 = Button(window_title, text="\n      Готов      \n", command=click_clear, bg="brown2")  
btn_1.grid(column=0, row=6) 
title_list_sword_2 = Label(window_title, text="\n<Ξ≥≤≥≤≥≤ΞΞΞΞΞΞΞΞΞΞ)|§₪₪₪₪ס", 
                           font="Roboto 15", fg="Red", bg="#FFCBBB").grid(column=0, row=10)

window_title.mainloop()


class Thing:
    def __init__(self, name: str,
                 add_defense: Optional[float] = None,
                 add_hp: Optional[float] = None,
                 add_physical_damage: Optional[float] = None,                 
                 add_magic_damage: Optional[float] = None,
                 add_fire_damage: Optional[float] = None,
                 add_poison_damage: Optional[float] = None,
                 add_bow_damage: Optional[float] = None) -> None:

                 self.name = name
                 self.add_defense = add_defense
                 self.add_hp = add_hp
                 self.add_physical_damage = add_physical_damage
                 self.add_magic_damage = add_magic_damage
                 self.add_fire_damage = add_fire_damage
                 self.add_poison_damage = add_poison_damage


class Person:
    def __init__(self, name: str,
                hp: float,
                damage: float,
                defense: float,
                magic_damage: Optional[float] = None
                ) -> None:
                
                self.name = name
                self.hp = hp
                self.damage = damage
                self.defense = defense
                self.things: List[Any] = []

    def setThings(self, things):
        self.things.append(things)
        self.add_characteristics(things)

    def add_characteristics(self, things):
        for thing in self.things:
            if thing.add_physical_damage is not None:
                self.damage += thing.add_physical_damage
            elif thing.add_defense is not None:
                self.defense += thing.add_defense
            elif thing.add_poison_damage is not None:
                self.damage = thing.add_poison_damage*10
            elif thing.add_fire_damage is not None:
                self.damage = thing.add_fire_damage*15
            try:
                if thing.add_magic_damage is not None:
                    self.magic_damage += thing.add_magic_damage
            except AttributeError:
                continue

    def attack_damage(self, attack_damage) -> None:
        self.hp = (self.hp - (attack_damage - attack_damage*defense))


class Paladin(Person):
    def __init__(self, name, hp: float, damage: float, defense: float) -> None:
        super().__init__(name, hp, damage, defense)
        self.hp = hp*2
        self.defense = defense*2


class Warrior(Person):
    def __init__(self, name, hp: float, damage: float, defense: float) -> None:
        super().__init__(name, hp, damage, defense)
        self.damage = damage*2


class Wizard(Person):
    def __init__(self, name, hp: float, damage: float, defense: float, magic_damage: float) -> None:
        super().__init__(name, hp, damage, defense)
        self.magic_damage = magic_damage


class Archer(Person):
    def __init__(self, name, hp: float, damage: float, defense: float, bow_damage: float) -> None:
        super().__init__(name, hp, damage, defense)
        self.bow_damage = bow_damage

classes = [Paladin, Warrior, Wizard, Archer]
list_heroes: List[Person] = []

heroes = ["Иля", "Жизнемир", "Любор", "Сивояр", "Преслав", "Мирограй", "Всеволод", "Вольга",
          "Буй-тур", "Эрна", "Фроди", "Глум", "Ворон", "Волк", "Всеград", "Татимир", "Разумник",
          "Путимир", "Милодух", "Лесьяр"]

artifacts = {0: Thing(name="Меч мощи", add_physical_damage=rdm.randint(20,40)),
1:Thing(name="Секира горного короля", add_physical_damage=rdm.randint(20, 40)),
2: Thing(name="Посох пропавшего волшебника", add_magic_damage=rdm.randint(20,40)),
3: Thing(name="Лук из рога единорога", add_physical_damage=rdm.randint(20,40)),
4: Thing(name="Посох преисподней", add_magic_damage=rdm.randint(30,50)),
5: Thing(name="Пламенный язык дракона", add_fire_damage=rdm.randint(1,5), 
                                                                add_physical_damage=rdm.randint(30,50)),
6: Thing(name="Щит короля гномов", add_defense=(rdm.randint(20, 60)/100)),
7: Thing(name="Кольцо храбрости", add_defense=(rdm.randint(20,40)/100)),
8: Thing(name="Доспехи рыцаря", add_defense=(rdm.randint(30,50)/100)),
9: Thing(name="Лунный клинок", add_physical_damage=rdm.randint(20, 50),
                                                add_poison_damage=rdm.randint(3, 10)),
10: Thing(name="Том магии Хаоса", add_magic_damage=rdm.randint(30, 60)),
11: Thing(name="Корона горного короля", add_defense=rdm.randint(30, 60)),
12: Thing(name="Меч короля Артура", add_physical_damage=rdm.randint(50, 70)),
13: Thing(name="Плащ ассасина", add_poison_damage=rdm.randint(4, 10), add_defense=rdm.randint(20, 50)),
14: Thing(name="Перо ангела", add_physical_damage=rdm.randint(30, 70)),
15: Thing(name="Кольцо бессмертия", add_hp=rdm.randint(40, 100))
}

window = Tk()  
window.title("Battle-arena")
window["bg"]= "#FFCBBB"
window.geometry('340x550')
my_list = Tk()
my_list.title("Events")
my_list.geometry('600x600')

def next():
    window.destroy()

_list = scrolledtext.ScrolledText(window, width=40, height=200)
_list.grid(column=0, row=0)
_list.pack()
scroll = Scrollbar(command=_list.yview)
scroll.pack(side=LEFT, fill=Y)
events = scrolledtext.ScrolledText(my_list)
events.grid(column=0, row=0)
events.pack()
scroll_events = Scrollbar(command=events.yview)
scroll_events.pack(fill=Y)

_list.insert(INSERT, "Участники битвы:\n")

for i in range(10):
    name: str = rdm.choice(heroes)
    heroes.remove(name)
    hp: float = rdm.randint(30, 150)
    damage: float = rdm.randint(10, 60)
    defense: float = rdm.randint(0, 9) / 100
    hero_class = rdm.choice(classes)
    if hero_class == Paladin:
        hero = hero_class(name, hp, damage, defense)
        list_heroes.append(hero)
        _list.insert(INSERT,(f"Герой {hero.name}:\n"
              f"            Класс: Паладин\n"
              f"            Количество здоровья: {hero.hp}\n"
              f"            Урон: {hero.damage}\n"
              f"            Коэффициент защиты: {hero.defense}\n"))
    elif hero_class == Wizard:
        magic_damage = rdm.randint(40, 70)
        hero = hero_class(name, hp, damage, defense, magic_damage)
        list_heroes.append(hero)
        _list.insert(INSERT,(f"Герой {hero.name}:\n"
              f"            Класс: Маг\n"
              f"            Количество здоровья: {hero.hp}\n"
              f"            Урон: {hero.damage}\n"
              f"            Коэффициент защиты: {hero.defense}\n"
              f"            Магический урон: {magic_damage}\n"))
    elif hero_class == Warrior:
        hero = hero_class(name, hp, damage, defense)
        list_heroes.append(hero)
        _list.insert(INSERT,(f"Герой {hero.name}:\n"
              f"            Класс: Воин\n"
              f"            Количество здоровья: {hero.hp}\n"
              f"            Урон: {hero.damage}\n"
              f"            Коэффициент защиты: {hero.defense}\n"))
    elif hero_class == Archer:
        bow_damage = rdm.randint(30, 60)
        hero = hero_class(name, hp, damage, defense, bow_damage)
        list_heroes.append(hero)
        _list.insert(INSERT,(f"Герой {hero.name}:\n"
              f"            Класс: Лучник\n"
              f"            Количество здоровья: {hero.hp}\n"
              f"            Урон: {hero.damage}\n"
              f"            Коэффициент защиты: {hero.defense}\n"
              f"            Урон от лука: {bow_damage}\n"))
_list.config(state = DISABLED)


for number in range(rdm.randint(0, 15)):
    random_hero = rdm.choice(list_heroes)
    time_list: List[Any] = []
    time_list = list_heroes
    if len(random_hero.things) > 4:
        time_list.remove[time_list]
    if len(random_hero.things) < 4:
        artifact = artifacts[rdm.randint(0,15)]
        if artifact not in random_hero.things:
            random_hero.setThings(artifact)
            if artifact.add_physical_damage is not None:
                events.insert(0.0, f"Артефакт увеличивает физический урон на {artifact.add_physical_damage}\n")
                random_hero.add_characteristics(artifact)
            elif artifact.add_magic_damage is not None:
                events.insert(0.0, f"Артефакт увеличивает магичекий урон на {artifact.add_magic_damage}\n")
                random_hero.add_characteristics(artifact)
            elif artifact.add_fire_damage is not None:
                events.insert(0.0, f"Артефакт позволяет наносить огненный урон, количество урона: {artifact.add_fire_damage}\n")
                random_hero.add_characteristics(artifact)
            elif artifact.add_defense is not None:
                events.insert(0.0, f"Артефакт увеличивает показатель брони на {artifact.add_defense}\n")
                random_hero.add_characteristics(artifact)
            elif artifact.add_poison_damage is not None:
                events.insert(0.0, f"Артефакт позволяет наносить урон ядом, количество урона: {artifact.add_poison_damage}\n")
                random_hero.add_characteristics(artifact)
            elif artifact.add_hp is not None:
                events.insert(0.0, f"Артефакт увеличивает показатель здоровья на {artifact.add_hp}\n")
                random_hero.add_characteristics(artifact)
            events.insert(0.0,(f"----{artifact.name}----\n"))
            events.insert(0.0,(f"\nГерой {random_hero.name} по пути нашел:\n"))
            time.sleep(rdm.uniform(0.2, 0.5))
            events.update()
events.update()
events.insert(0.0, "\n\n\n             ДА НАЧНЕТСЯ БИТВА!              \n\n\n")
time.sleep(2)
events.update()


while len(list_heroes) != 1:
    try:
        person_1 = rdm.choice(list_heroes)
    except IndexError:
        break
    try:
        person_2 = rdm.choice(list_heroes)
    except IndexError:
        break
    if len(list_heroes) == 1:
        print("SJFKSHJFCNSDJK")
    if person_1 != person_2:
        events.insert(0.0, f"На ринг выходят {person_1.name} и {person_2.name}\n\n")
        a = 1
        while a == 1:
            i = rdm.randint(0, 1)
            if i == 0:
                events.insert(0.0, f"{person_2.name} наносит герою {person_1.name} урон в размере: {person_2.damage}\n")
                person_1.attack_damage(person_2.damage)
                time.sleep(0.5)
                events.update()
                if person_1.hp > 0:
                    events.insert(0.0, f"У героя {person_1.name} осталось  количество здоровья: {round(person_1.hp, 3)}\n")
            else:
                events.insert(0.0, f"{person_1.name} наносит герою {person_2.name} урон в размере: {person_1.damage}\n")
                person_2.attack_damage(person_1.damage)
                time.sleep(0.5)
                events.update()
                if person_2.hp > 0:
                    events.insert(0.0, f"У героя {person_2.name} осталось количество здоровья: {round(person_2.hp, 3)} \n")
            if person_1.hp < 0:
                events.insert(0.0, f"Герой {person_1.name} погиб...\n")
                time.sleep(0.5)
                events.update()
                list_heroes.remove(person_1)
                a = 0
            elif person_2.hp < 0:
                events.insert(0.0, f"Герой {person_2.name} погиб...\n")
                time.sleep(0.5)
                events.update()
                list_heroes.remove(person_2)
                a = 0

for i in list_heroes:
    events.insert(0.0, f"           \n\n\n\nПОБЕДИТЕЛЬ: ------- {i.name}-------      \n\n\n\n")

events.config(state = DISABLED)
events.mainloop()