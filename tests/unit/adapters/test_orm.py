from src.allocation.domain.model import OrderLine


def test_orderline_mapper_can_load_lines(session):
    expected = [
        OrderLine(order_id='order1', sku='RED-CHAIR', qty=12),
        OrderLine(order_id='order1', sku='RED-TABLE', qty=13),
        OrderLine(order_id='order2', sku='BLUE-LIPSTICK', qty=14),
    ]

    assert session.query(OrderLine).all() == expected


def test_orderline_mapper_can_save_lines(session):
    new_line = OrderLine(order_id='order1', sku='DECORATIVE-WIDGET', qty=12)
    session.add(new_line)
    session.commit()
    rows = list(session.execute('SELECT order_id, sku, qty FROM "order_lines"'))

    assert rows == [('order1', 'DECORATIVE-WIDGET', 12)]
