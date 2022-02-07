from datetime import date
from src.allocation.domain.model import Batch, OrderLine


def make_batch_and_line(sku: str, batch_qty: int, line_qty: int):
    return (
        Batch(ref="batch-001", sku=sku, qty=batch_qty, eta=date.today()),
        OrderLine(orderid="order-ref", sku=sku, qty=line_qty),
    )


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch, line = make_batch_and_line(sku="SMALL-TABLE", batch_qty=20, line_qty=2)
    batch.allocate(line)
    assert batch.available_quantity == 18


def test_can_allocate_if_available_greater_than_required():
    pass


def test_cannot_allocate_if_available_smaller_than_required():
    pass


def test_can_allocate_if_available_equal_to_required():
    pass


def test_cannot_allocate_if_skus_do_not_match():
    pass
