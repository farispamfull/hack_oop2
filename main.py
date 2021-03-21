from random import sample, randint, choice


class Person:
    limit_things = 4
    specialization = 'оффисный работник'
    arena = False

    def __init__(self, name, hp, damage, resist):
        self.name = name
        self.resist = resist
        self.damage = damage
        self.hp = hp
        self.things = []
        self.base_hp = hp
        # возможность привязать к арене сразу всех person и наследников через атрибут класса
        # тогда можно моментально без лишних действий вызвать сражения на арене
        if isinstance(self.arena, Arena):
            arena.boy += [self]

    def _append_things(self, thing):
        for stat in thing:
            self.resist += stat.resist
            self.damage += stat.damage
            self.hp += stat.hp

    def setThings(self, *things):
        limit = self.limit_things
        if len(self.things) == limit:
            return print('Уже есть 4 предмета, больше нельзя')
        if len(things) > limit:
            print('Добавили только первые 4 предмета. Больше нельзя.')
        self._append_things(things[:limit])
        self.things += [*things][:limit]

    def view_things(self):
        # выводим вещи с номером по которому потом их можно удалить
        for thing in enumerate(self.things, 1):
            print(f'({thing[0]})', thing[1])

    def del_things(self, *index):
        # принимаем номера или номер вещи и удаляем

        things = self.things
        
        for i in index:
            thing = things[i - 1] # смещение на 1, потому что индексы с 0 идут
            # добавляем вещь с отрицательными значениями, чтобы вычесть статы вещи
            self._append_things([-thing])

            del things[i - 1]

    def _dead(self):
        if self.hp > 0:
            return False
        else:
            return True

    def set_damage(self):
        return self.damage

    def get_damage(self, damage):
        final_damage = damage - damage * self.resist / 100
        self.hp -= final_damage
        # вовращаем статус смерти
        return self._dead()

    def _attack(self, opponent):
        damage = self.set_damage()
        result = opponent.get_damage(damage)
        hp = opponent.hp
        if not result:
            print(
                f'{self.name} нанес {damage} урона, оставив {opponent.name} {hp} здоровья')
            return result
        else:
            print(
                f'{self.name} нанес {damage} критического урона. Эта атака '
                f'была смертельной для {opponent.name}',
                end='\n\n')
            print(f'{self.name}, поздравляем тебя с победой в этом матче!')
            return result

    def __str__(self):
        return f'Имя: {self.name}\nСпецилизация: {self.specialization}\nCтаты: атака {self.damage} | защита {self.resist} | здоровье {self.hp}'


class Thing:

    def __init__(self, name, resist=0, damage=0, hp=0):
        self.name = name
        self.resist = resist
        self.damage = damage
        self.hp = hp

    def __neg__(self):
        self.resist = -self.resist
        self.damage = -self.damage
        self.hp = -self.hp
        return self

    # @classmethod
    # def _devil_thing(cls,name,resist,damage,hp):
    #     devil_thing=cls(name,-resist,-damage,-hp)
    #     return devil_thing

    def __str__(self):
        return f'{self.name} | защита +{self.resist} | атака +{self.damage} | здоровье +{self.hp}'


class Paladin(Person):
    specialization = 'Паладин'

    def __init__(self, name, hp, damage, resist):
        super().__init__(name, hp, damage, resist)
        self.hp = hp * 2
        self.resist = resist * 2


class Warrior(Person):
    specialization = 'Воин'

    def __init__(self, name, hp, damage, resist):
        super().__init__(name, hp, damage, resist)
        self.damage = damage * 2


#сущность арены
class Arena:
    def __init__(self, *boys):
        self.boy = [*boys]

    def reset_hp(self, fight1, fight2):
        fight1.hp = fight1.base_hp
        fight2.hp = fight2.base_hp
        
    # метод используется в методах sparring,one_sparring
    # возвращает проигравшего в конкретной схватке
    def fight(self, random_rivals):

        boy, boy2 = random_rivals
        loser = None
        while loser is None:
            #наносим по очереди урон пока не умрет один из участников
            if boy._attack(boy2):
                loser = boy2
            elif boy2._attack(boy):
                loser = boy
        #востанавливаем хп до базовых значений
        self.reset_hp(boy, boy2)
        return loser

    def add_rival(self, *boy):
        self.boy += boy

    def view_rivals(self):
        print('Наши бойцы')
        print('____________')
        if len(self.boy) == 0:
            print('у нас пока нет бойцов(')
        else:
            for boy in self.boy:
                print(boy, end='\n\n')

    def __str__(self):
        boys = len(self.boy)
        return f'сейчас на арене {boys}'

    def random_rivals(self):
        return sample(self.boy, 2)

    # одиночное сражение
    def one_sparring(self):
        random_rivals = self.random_rivals()
        loser = self.fight(random_rivals)
        self.boy.remove(loser)
        if len(self.boy) == 1:
            print(f'Поздравляем победителя Арены:\n{self.boy.pop()}')

    # сражения среди всех, кто есть
    # выводит или возвращает победителя всех сражений.Арена при этом становится пустой
    def sparring(self, flag=False):

        while len(self.boy) > 2:
            random_rivals = self.random_rivals()
            loser = self.fight(random_rivals) #убираем с арены проигравшего
            self.boy.remove(loser)
        #сюда пойдем когда останется 2 бойца на арене 
        random_rivals = self.random_rivals()
        loser = self.fight(random_rivals)
        self.boy.remove(loser)
        print()
        winner = self.boy.pop()
        print(
            f'Поздравляем победителя арены:\n{winner}\nУ него были такие вещи:')
        winner.view_things()
        print('______________________')
        # если хочется вернуть супербойца
        if flag:
            return winner


# класс, который случайно генерирует нужные нам сущности
class RandomTools:
    specialization = [Person, Warrior, Paladin]
    #можно как угодно передавать в эти переменные списки. Можно неявно.
    persons = [
        'Strawberry',
        'Sunshine',
        'Sweet cheeks',
        'Tender lioness',
        'Little monster',
        'Lady luck',
        'Funny Bunny',
        'Flowers lover',
        'Eco prettiness',
        'Charming hostess',
        'Banshee',
        'Warrior',
        'Secret player',
        'Pugilist',
        'Lucky Guy',
        'Help bringer',
        'Flame host ',
        'dragon',
        'Detector',
        'Cowboy'
    ]
    things = [
        'Boots',
        'Coat',
        'Dress',
        'Jacket',
        'Jeans',
        'Shirt',
        'Shoes',
        'Skirt',
        'Fur coat',
        'Waistcoat',
        'Bananas',
        'axe',
        'rapier',
        'machete',
        'dagger',
        'rifle'
    ]

    # возвращаем список случаных характеристик
    def random_stat():
        name = choice(RandomTools.persons)
        hp, damage, resist = (randint(2, 7) if stat != 0 else randint(15, 30)
                              for stat in range(3))
        return [name, hp, damage, resist]

    # возвращаем список случайных бойцов, количество можно задать параметром
    def random_rivals(amount=10):
        rivals = []
        for i in range(amount):
            rival = choice(RandomTools.specialization)
            rival = rival(*RandomTools.random_stat())

            rival.setThings(*RandomTools.random_things())
            rivals += [rival]
        return rivals

    # возвращает список случайных предметов, не больше 4
    def random_things():
        things = []
        limit = Person.limit_things
        for i in range(randint(1, limit)):
            name = choice(RandomTools.things)
            resist, damage, hp = (
                randint(0, 15) if stat != 0 else randint(0, 10) for stat in
                range(3))
            things.append(Thing(name, resist, damage, hp))
        return things
    #один случайный боей
    def one_rivals():
        return RandomTools.random_rivals(1).pop()


    
# Пример вызова рандомных сражений
arena = Arena()

rivals = RandomTools.random_rivals(10)
arena.add_rival(*rivals)
a = arena.sparring(True)

# пример обычного вызова
arena2 = Arena()
alex = Warrior('alex', 10, 10, 14)
ring = Thing('ring', 30, 2, 2)
alex.setThings(ring, ring)
alex.view_things()
Jesus=RandomTools.one_rivals()   #один рандомный боец
arena2.add_rival(alex,Jesus)
arena2.view_rivals()
arena2.one_sparring()

#Сражение на 3 арене между победителями двух предыдущих
arena=Arena()
arena2=Arena()
arena3=Arena()
arena.add_rival(*RandomTools.random_rivals(14))
arena2.add_rival(*RandomTools.random_rivals(14))
one_winner=arena.sparring(True)
two_winner=arena2.sparring(True)
arena3.add_rival(one_winner,two_winner)
print('_________________________________________')
arena3.view_rivals()
arena3.one_sparring()

#делаем привязку к арене через поле класса
#Делать лучше тогда, когда есть только одна арена, иначе бойцы из других арен привяжуться к нашей
arena=Arena()
Person.arena=arena
RandomTools.random_rivals(16) # в арене сразу появится 16 бойцов
print(arena)
arena.sparring() #можно сразу вызывать сражения
