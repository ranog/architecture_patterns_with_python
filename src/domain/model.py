from datetime import date
from dataclasses import dataclass
from typing import Optional, NewType
from src.exceptions.model import AllocateError, DeallocateError

Reference = NewType('Reference', str)
Sku = NewType('Sku', str)
Quantity = NewType('Quantity', int)
Orderid = NewType('Orderid', str)


@dataclass(frozen=True)
class OrderLine:
    orderid: Orderid
    sku: Sku
    quantity: Quantity


class Batch:

    def __init__(
        self,
        reference: Reference,
        sku: Sku,
        quantity: Quantity,
        eta: Optional[date],
    ):
        self.reference = reference
        self.sku = sku
        self.eta = eta
        self._purchased_quantity = quantity
        self._allocations = set()

    def __eq__(self, other) -> bool:
        if not isinstance(other, Batch):
            return False
        return other.reference == self.reference

    def __hash__(self) -> int:
        return hash(self.reference)

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
