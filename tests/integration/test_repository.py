from src.allocation.domain.model import Batch


def test_repository_can_save_a_batch(session):
    batch = Batch(ref='batch1', sku='RUSTY-SOAPDISH', qty=100, eta=None)
