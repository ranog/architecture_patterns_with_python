from src.allocation.domain.model import OrderLine
from tests.seeds import ORDER_LINES_SEED


def test_orderline_mapper_can_load_lines(session):
    session.execute(ORDER_LINES_SEED)
    order_line_1 = OrderLine(order_id='order1', sku='RED-CHAIR', qty=12)
    order_line_1.id = 1
    order_line_2 = OrderLine(order_id='order2', sku='RED-TABLE', qty=13)
    order_line_2.id = 2
    order_line_3 = OrderLine(order_id='order3', sku='BLUE-LIPSTICK', qty=14)
    order_line_3.id = 3
    order_line_4 = OrderLine(order_id='order4', sku='GENERIC-SOFA', qty=12)
    order_line_4.id = 4
    expected = [order_line_1, order_line_2, order_line_3, order_line_4]
    order_lines = session.query(OrderLine).order_by(OrderLine.id).all()
    assert order_lines == expected


def test_orderline_mapper_can_save_lines(session):
    new_line = OrderLine(order_id='order1', sku='DECORATIVE-WIDGET', qty=12)
    session.add(new_line)
    session.commit()
    rows = list(session.execute('SELECT order_id, sku, qty FROM "order_lines"'))

    assert rows == [('order1', 'DECORATIVE-WIDGET', 12)]
