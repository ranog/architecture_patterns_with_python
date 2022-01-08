from datetime import date
from src.domain.model import Batch, OrderLine


def test_allocating_to_a_batch_reduces_the_available_quantity():
    batch = Batch(reference='batch-001', sku='SMALL-TABLE', quantity=20, eta=date.today())
    line = OrderLine(orderid='order-ref', sku='SMALL-TABLE', quantity=2)

    batch.allocate(line)

    assert batch.available_quantity == 18
