from datetime import date
from src.domain.model import Batch, OrderLine


def _make_batch_and_line(sku: str, batch_qty: int, line_qty: int):
    return (
        Batch(reference='batch-001', sku=sku, quantity=batch_qty, eta=date.today()),
        OrderLine(orderid='order-ref', sku=sku, quantity=line_qty),
    )


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch, line = _make_batch_and_line(sku='SMALL-TABLE', batch_qty=20, line_qty=2)
    batch.allocate(line)
    assert batch.available_quantity == 18


def test_can_allocate_if_available_greater_than_required():
    large_batch, small_line = _make_batch_and_line(sku="ELEGANT-LAMP", batch_qty=20, line_qty=2)
    assert large_batch.can_allocate(small_line)


def test_cannot_allocate_if_available_smaller_than_required():
    small_batch, large_line = _make_batch_and_line(sku="ELEGANT-LAMP", batch_qty=2, line_qty=20)
    assert small_batch.can_allocate(large_line) is False


def test_can_allocate_if_available_equal_to_required():
    batch, line = _make_batch_and_line(sku="ELEGANT-LAMP", batch_qty=2, line_qty=2)
    assert batch.can_allocate(line)


def test_cannot_allocate_if_skus_do_not_match():
    batch = Batch(reference="batch-001", sku="UNCOMFORTABLE-CHAIR", quantity=100, eta=None)
    different_sku_line = OrderLine(orderid="order-123", sku="EXPENSIVE-TOASTER", quantity=10)
    assert batch.can_allocate(different_sku_line) is False


def test_can_only_deallocate_allocated_lines():
    batch, unallocated_line = _make_batch_and_line(sku='DECORATIVE-TRINKET', batch_qty=20, line_qty=2)
    batch.deallocate(unallocated_line)
    assert batch.available_quantity == 20
