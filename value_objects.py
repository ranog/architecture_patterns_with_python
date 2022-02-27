from dataclasses import dataclass
from typing import NamedTuple
from collections import namedtuple


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str


class Money(NamedTuple):
    currency: str
    value: int


Line = namedtuple('Line', ['sku', 'qty'])


def test_equality():
    assert Money(currency='gbp', value=10)
    assert Name(first_name='Harry', surname='Percival') != Name(first_name='Bob', surname='Gregory')
    assert Line(sku='RED-CHAIR', qty=5) == Line(sku='RED-CHAIR', qty=5)
