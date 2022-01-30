from src.domain.model import Batch
from src.adapters.repositories import repository


def test_repository_can_save_a_batch(session):
    batch = Batch(reference='batch1', sku='RUSTY-SOAPDISH', quantity=100, eta=None)

    repo = repository.SqlAlchemyRepository(session)
    repo.add(batch)

    rows = list(session.execute('SELECT reference, sku, _purchased_quantity, eta FROM "batches"'))
    assert rows == [('batch1', 'RUSTY-SOAPDISH', 100, None)]
