from enum import Enum, auto

DESCRIPTION = (
    'Glamorous',
    'Beautiful',
    'Foolish',
    'Awesome',
    'Disgusting',
    'Dumb',
    'Unhappy',
    'Numb',
    'Dirty',
    'Schwifty',
)


class AttackStatus(Enum):
    HIT = auto(),
    KILL = auto(),
    DODGE = auto(),
