from dataclasses import dataclass
from collections import namedtuple

import pytest


@dataclass(frozen=True)
class Name:
    first_name: str
    surname: str


class Person:

    def __init__(self, name: Name):
        self.name = name


@dataclass(frozen=True)
class Money:
    currency: str
    value: int

    def __add__(self, other):
        if other.currency != self.currency:
            raise ValueError(f'Cannot add {self.currency} to {other.currency}')
        return Money(self.currency, self.value + other.value)


Line = namedtuple('Line', ['sku', 'qty'])


def test_equality():
    assert Money(currency='gbp', value=10)
    assert Name(first_name='Harry', surname='Percival') != Name(first_name='Bob', surname='Gregory')
    assert Line(sku='RED-CHAIR', qty=5) == Line(sku='RED-CHAIR', qty=5)


fiver = Money(currency='gbp', value=5)
tenner = Money(currency='gbp', value=10)


def test_can_add_money_values_for_the_same_currency():
    assert fiver.value + fiver.value == tenner.value


def test_can_subtract_money_values():
    assert tenner.value - fiver.value == fiver.value


def test_adding_different_currencies_fails():
    with pytest.raises(ValueError):
        Money(currency='usd', value=10) + Money(currency='gbp', value=10)


def test_can_multiply_money_by_a_number():
    assert fiver.value * 5 == Money(currency='gbp', value=25).value


def test_multiplying_two_money_values_is_an_error():
    with pytest.raises(TypeError):
        tenner * fiver


def test_name_equality():
    assert Name(first_name='Harry', surname='Percival') != Name(first_name='Barry', surname='Percival')


def test_barry_is_harry():
    harry = Person(name=Name(first_name='Harry', surname='Percival'))
    barry = harry

    barry.name = Name(first_name='Barry', surname='Percival')

    assert harry is barry and barry is harry
