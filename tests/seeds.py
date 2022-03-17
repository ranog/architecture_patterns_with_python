CREATE_ORDER_LINES_TABLE = """
CREATE TABLE IF NOT EXISTS "order_lines" (
    orderid varchar(255) NULL,
    sku varchar(255) NULL,
    qty int4 NULL,
    CONSTRAINT "order_lines_pkey" PRIMARY KEY (orderid)
);
TRUNCATE TABLE "order_lines";
"""

ORDER_LINES_SEED = """
INSERT INTO
    "order_lines" (orderid, sku, qty)
VALUES
    ('order1','RED-CHAIR',12),
    ('order2','RED-TABLE',13),
    ('order3','BLUE-LIPSTICK',14),
    ('order4','DECORATIVE-WIDGET',12)
"""


def populate_order_lines(session):
    session.execute(CREATE_ORDER_LINES_TABLE)
    session.execute(ORDER_LINES_SEED)
