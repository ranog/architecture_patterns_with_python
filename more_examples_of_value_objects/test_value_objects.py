import pytest
from more_examples_of_value_objects.value_objects import Money, Name, Line, Person

fiver = Money('gbp', 5)
tenner = Money('gbp', 10)


def test_barry_is_harry():
    harry = Person(Name('Harry', 'Percival'))
    barry = harry
    barry.name = Name('Barry', 'Percival')
    assert harry is barry and barry is harry


def test_name_equality():
    assert Name('Harry', 'Percival') != Name('Barry', 'Percival')


def test_equality():
    assert Money('gbp', 10) == Money('gbp', 10)
    assert Name('Harry', 'Percival') != Name('Bob', 'Gregory')
    assert Line('RED-CHAIR', 5) == Line('RED-CHAIR', 5)


def test_can_add_money_values_for_the_same_currency():
    assert fiver.value + fiver.value == tenner.value


def test_can_subtract_money_values():
    assert tenner.value - fiver.value == fiver.value


def test_adding_different_currencies_fails():
    with pytest.raises(ValueError):
        Money('usd', 10) + Money('gbp', 10)


def test_can_multiply_money_by_a_number():
    assert fiver.value * 5 == Money('gbp', 25).value


def test_multiplying_two_money_values_is_an_error():
    with pytest.raises(TypeError):
        tenner * fiver
