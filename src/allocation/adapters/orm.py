from sqlalchemy import Column, Integer, String, Table
from sqlalchemy.orm import registry
from src.allocation.domain import model

mapper_registry = registry()

order_lines = Table(
    'order_lines',
    mapper_registry.metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(250)),
    Column('qty', Integer, nullable=False),
    Column('order_id', String(250)),
)


def start_mappers():
    mapper_registry.map_imperatively(model.OrderLine, order_lines)
