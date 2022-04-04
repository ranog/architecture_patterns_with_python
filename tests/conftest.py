import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, clear_mappers
from src.allocation.adapters.orm import start_mappers

from tests.seeds import CREATE_BATCHES_TABLE, CREATE_ORDER_LINES_TABLE

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')


@pytest.fixture
def session():
    start_mappers()
    with Session(engine) as session:
        session.execute(CREATE_ORDER_LINES_TABLE)
        session.execute(CREATE_BATCHES_TABLE)
        yield session
    clear_mappers()
