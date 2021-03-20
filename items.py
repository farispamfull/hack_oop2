class Thing():
    MAX_PROTECTION_PERCENT = 0.1

    def __init__(
        self,
        name: str,
        attack: int,
        protection_percent: float,
        health: int
    ):
        self.name = name
        self.attack = attack
        if protection_percent > self.MAX_PROTECTION_PERCENT:
            protection_percent = self.MAX_PROTECTION_PERCENT
        self.protection_percent = protection_percent
        self.health = health

    def __repr__(self):
        return (
            f'Thing({self.name}, {self.attack}, '
            f'{self.protection_percent}, {self.health})'
        )
