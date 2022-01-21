from collections import namedtuple
from dataclasses import dataclass


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str


@dataclass(frozen=True)
class Money:
    currency: str
    value: int

    def __add__(self, other):
        if other.currency != self.currency:
            raise ValueError(f'Cannot add {self.currency} to {other.currency}')
        return Money(self.currency, self.value + other.value)


Line = namedtuple('Line', ['sku', 'qty'])


class Person:

    def __init__(self, name: Name):
        self.name = name
