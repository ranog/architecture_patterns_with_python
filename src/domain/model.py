from datetime import date
from dataclasses import dataclass
from typing import Optional

from src.exceptions.model import AllocateError, DeallocateError


@dataclass(frozen=True)
class OrderLine:
    orderid: str
    sku: str
    quantity: int


class Batch:

    def __init__(
        self,
        reference: str,
        sku: str,
        quantity: int,
        eta: Optional[date],
    ):
        self.reference = reference
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = quantity
        self._allocations = set()

    def allocate(self, line: OrderLine):
        if self.can_allocate(line=line):
            self._allocations.add(line)
        else:
            raise AllocateError('Error when allocate')

    def deallocate(self, line: OrderLine) -> None:
        if line in self._allocations:
            self._allocations.remove(line)
        else:
            raise DeallocateError('Error when deallocate')

    @property
    def allocated_quantity(self) -> int:
        return sum(line.quantity for line in self._allocations)

    @property
    def available_quantity(self) -> int:
        return self._purchased_quantity - self.allocated_quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.quantity
