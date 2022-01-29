import logging
from src.domain import model
from sqlalchemy import (
    Table,
    MetaData,
    Column,
    Integer,
    String,
    # Date,
    ForeignKey,
)
from sqlalchemy.orm import mapper  # relationship

logger = logging.getLogger(__name__)

metadata = MetaData()

order_lines = Table(
    "order_lines",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("sku", String(255)),
    Column("qty", Integer, nullable=False),
    Column("orderid", String(255)),
)

allocations = Table(
    "allocations",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("orderline_id", ForeignKey("order_lines.id")),
    Column("batch_id", ForeignKey("batches.id")),
)


def start_mappers():
    lines_mapper = mapper(model.OrderLine, order_lines)
    lines_mapper
