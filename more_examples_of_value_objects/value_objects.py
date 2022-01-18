from collections import namedtuple
from dataclasses import dataclass
from typing import NamedTuple


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str


class Money(NamedTuple):
    currency: str
    value: int


Line = namedtuple('Line', ['sku', 'qty'])


class Person:

    def __init__(self, name: Name):
        self.name = name
