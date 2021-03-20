class Item:

    '''
        Преименованный класс Thing
        Позволяет созадавать вещи, выводить их статы
    '''

    def __init__(self, info, attack=0, defence=0, additional_hp=0,
                 mode='basic'):
        if mode == 'basic':
            self.name = info
            self.attack = attack
            self.defence = defence
            self.additional_hp = additional_hp
        elif mode == 'dict':
            self.name = info['name']
            self.attack = int(info['attack'])
            self.defence = int(info['defence'])
            self.additional_hp = int(info['additional_hp'])

    def __str__(self):
        return f'{self.name}'

    def show_stats(self):
        return (f'{self.name}:\n'
                f'Урон: {self.attack}\n'
                f'Защита: {self.defence}\n'
                f'Бонусное здоровье: {self.additional_hp}')

    def get_raryty(self):
        return self.attack+self.defence+self.additional_hp
