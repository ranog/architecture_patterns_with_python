from src.allocation.domain.model import Batch
import abc


class AbstractRepository(abc.ABC):

    @abc.abstractmethod
    def add(self, batch: Batch):
        raise NotImplementedError

    @abc.abstractmethod
    def get(self, reference) -> Batch:
        raise NotImplementedError


class SqlAlchemyRepository:

    def __init__(self, batch: Batch) -> None:
        self.batch = batch

    def add(self, batch: Batch):
        pass
