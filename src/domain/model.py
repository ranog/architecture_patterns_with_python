from datetime import datetime
from dataclasses import dataclass
from typing import Optional


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
        eta: Optional[datetime],
    ):
        self.reference = reference
        self.sku = sku
        self.available_quantity = quantity
        self.eta = eta

    def allocate(self, line: OrderLine):
        self.available_quantity -= line.quantity

    def can_allocate(self, line: OrderLine) -> bool:
        return self.sku == line.sku and self.available_quantity >= line.quantity

    def deallocate(self, line: OrderLine):
        pass
