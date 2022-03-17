from src.allocation.domain.model import OrderLine


def test_orderline_mapper_can_load_lines(session):
    session.execute(
        "INSERT INTO order_lines (orderid, sku, qty) VALUES "
        '("order1", "RED-CHAIR", 12),'
        '("order1", "RED-TABLE", 13),'
        '("order2", "BLUE-LIPSTICK", 14)'
    )
    expected = [
        OrderLine(orderid='order1', sku='RED-CHAIR', qty=12),
        OrderLine(orderid='order1', sku='RED-TABLE', qty=13),
        OrderLine(orderid='order2', sku='BLUE-LIPSTICK', qty=14),
    ]

    assert session.query(OrderLine).all() == expected


def test_orderline_mapper_can_save_lines(session):
    new_line = OrderLine(orderid='order1', sku='DECORATIVE-WIDGET', qty=12)
    session.add(new_line)
    session.commit()
    rows = list(session.execute('SELECT orderid, sku, qty FROM "order_lines"'))

    assert rows == [('order1', 'DECORATIVE-WIDGET', 12)]
