from sqlalchemy import Column, Integer, MetaData, String, Table
from sqlalchemy.orm import mapper
from src.allocation.domain import model

metadata = MetaData()

order_lines = Table(
    'order_lines',
    metadata,
    Column('id', Integer, primary_key=True, autoincrement=True),
    Column('sku', String(250)),
    Column('qty', Integer, nullable=False),
    Column('order_id', String(250)),
)

...


def start_mappers():
    lines_mapper = mapper(model.OrderLine, order_lines)
    return lines_mapper
