from pytest import Session
from src.allocation.domain.model import Batch
import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, batch: Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> Batch:
        raise NotImplementedError


class SqlAlchemyRepository(AbstractRepository):

    def __init__(self, session: Session) -> None:
        self.session = session

    def add(self, batch: Batch):
        self.session.add(batch)

    def get(self, reference: str):
        return self.session.query(Batch).filter_by(reference=reference).one()

    def list(self):
        return self.session.query(Batch).all()
