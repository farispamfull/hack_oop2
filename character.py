class Character:

    '''
        Преименованный класс Person
        Позволяет созадавать существ, выводить их статы и инвентарь
        А так же содержит методы по работе с вещами
    '''

    def __init__(self, hp, base_attack, base_defence, name='Noname'):
        self.type = 'Существо'
        self.name = name
        self.base_hp = hp
        self.full_hp = hp
        self.current_hp = hp
        self.base_attack = base_attack
        self.base_defence = base_defence
        self.full_attack = base_attack
        self.full_defence = base_defence
        self.items = []

    def __str__(self):
        return (f'{self.type} {self.name}\n'
                f'Здоровье: {self.base_hp}\n'
                f'Атака: {self.base_attack}\n'
                f'Защита: {self.base_defence}\n')

    def show_title(self):
        return f'{self.type} {self.name}'

    def show_inventory(self):
        return('\n'.join(item.show_stats() +
               '\n' for item in self.items))

    def show_full_stats(self):
        return (f'\n{self.type} {self.name}\n'
                f'Здоровье: {self.current_hp}/{self.full_hp}\n'
                f'Атака: {self.full_attack}\n'
                f'Защита: {self.full_defence}\n')

    def set_items(self, items):
        self.items = items
        for item in self.items:
            self.add_item(item)

    def add_item(self, item):
        if len(self.items) >= 4:
            self.drop_item()
        self.items.append(item)
        self.full_attack += item.attack
        self.full_defence += item.defence
        self.full_hp += item.additional_hp
        self.current_hp += item.additional_hp

    def drop_item(self):
        dropped_item = self.items.pop()
        self.full_attack -= dropped_item.attack
        self.full_defence -= dropped_item.defence
        self.full_hp -= dropped_item.additional_hp
        self.current_hp -= dropped_item.additional_hp
        return dropped_item

    def get_damage(self):
        return self.full_attack

    def recieve_damage(self, damage):
        '''
            Метод получения урона
            Формула для применения брони изменена на armor/(100+armor)
            Таким образом броня может расти до бесконечности
        '''
        recieved_damage = int(damage - damage * self.full_defence /
                              (self.full_defence+100))
        self.current_hp = self.current_hp - recieved_damage
        if self.current_hp > 0:
            return recieved_damage
        return 'Dead'


class Paladin(Character):
    def __init__(self, hp, base_attack, base_defence, name='Noname'):
        super().__init__(hp, base_attack, base_defence, name)
        self.type = 'Паладин'
        self.base_hp = hp*2
        self.full_hp = hp*2
        self.current_hp = hp*2
        self.base_defence = base_defence*2
        self.full_defence = base_defence*2


class Warrior(Character):
    def __init__(self, hp, base_attack, base_defence, name='Noname'):
        super().__init__(hp, base_attack, base_defence, name)
        self.type = 'Воин'
        self.base_attack = base_attack*2
        self.full_attack = base_attack*2
