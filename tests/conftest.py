import pytest
from sqlalchemy import create_engine
from sqlalchemy.orm import Session
from tests.seeds import populate_order_lines

engine = create_engine('postgresql://postgres:postgres@localhost:5432/postgres')


@pytest.fixture
def session():
    with Session(engine) as session:
        populate_order_lines(session)
        yield session
