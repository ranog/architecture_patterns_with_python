from src.allocation.adapters.repository import SqlAlchemyRepository
from src.allocation.domain.model import Batch


def test_repository_can_save_a_batch(session):
    batch = Batch(ref='batch1', sku='RUSTY-SOAPDISH', qty=100, eta=None)

    repo = SqlAlchemyRepository(session)
    repo.add(batch)
    session.commit()

    rows = session.execute('SELECT reference, sku, _purchased_quantity, eta FROM "batches"')

    assert list(rows) == [('batch1', 'RUSTY-SOAPDISH', 100, None)]
