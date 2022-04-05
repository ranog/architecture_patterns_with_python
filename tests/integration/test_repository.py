from src.allocation.adapters.repository import SqlAlchemyRepository
from src.allocation.domain.model import Batch, OrderLine
from tests.seeds import BATCHES_SEED, ORDER_LINES_SEED


def test_repository_can_save_a_batch(session):
    session.execute(BATCHES_SEED)
    rows = session.execute('SELECT reference, sku, _purchased_quantity, eta FROM "batches"')
    batch_expectation = [('batch1', 'RUSTY-SOAPDISH', 100, None)]
    assert list(rows) == batch_expectation


def insert_order_line(session):
    session.execute(ORDER_LINES_SEED)
    [[orderline_id]] = session.execute(
        "SELECT id FROM order_lines WHERE order_id=:order_id AND sku=:sku",
        dict(order_id="order4", sku="GENERIC-SOFA"),
    )
    return orderline_id


def insert_batch(session, batch_id):
    ...


def insert_allocation(session, orderline_id, batch1_id):
    ...


def test_repository_can_retrieve_a_batch_with_allocations(session):
    orderline_id = insert_order_line(session=session)
    batch1_id = insert_batch(session=session, batch_id='batch1')
    insert_batch(session=session, batch_id='batch2')
    insert_allocation(session, orderline_id, batch1_id)

    repo = SqlAlchemyRepository(session)
    retrieved = repo.get('batch1')

    expected = Batch(ref='batch1', sku='GENERIC-SOFA', qty=100, eta=None)

    assert retrieved == expected
    assert retrieved.sku == expected.sku
    assert retrieved._purchased_quantity == expected._purchased_quantity
    assert retrieved._allocations == {OrderLine("order4", "GENERIC-SOFA", 12)}
