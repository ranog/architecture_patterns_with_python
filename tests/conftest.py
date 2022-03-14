import pytest

from sqlalchemy import create_engine
from sqlalchemy.orm import Session


@pytest.fixture
def session():
    engine = create_engine('postgresql://scott:tiger@localhost/')
    with Session(engine) as session:
        session.add(some_object)
        session.add(some_other_object)
        session.commit()
