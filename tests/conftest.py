import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session, clear_mappers
from src.allocation.adapters.orm import start_mappers

from tests.seeds import CREATE_ORDER_LINES_TABLE, ORDER_LINES_SEED

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')


@pytest.fixture
@pytest.mark.usefixtures('mappers')
def session():
    with Session(engine) as session:
        session.execute(CREATE_ORDER_LINES_TABLE)
        session.execute(ORDER_LINES_SEED)
        yield session


@pytest.fixture
def mappers():
    start_mappers()
    yield
    clear_mappers()
