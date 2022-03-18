CREATE_ORDER_LINES_TABLE = """
CREATE TABLE IF NOT EXISTS "order_lines" (
    id int4,
    order_id varchar(255),
    sku varchar(255),
    qty int4,
    CONSTRAINT "order_lines_pkey" PRIMARY KEY (id)
);
TRUNCATE TABLE "order_lines";
"""

ORDER_LINES_SEED = """
INSERT INTO
    "order_lines" (id, order_id, sku, qty)
VALUES
    (1,'order1','RED-CHAIR',12),
    (2,'order2','RED-TABLE',13),
    (3,'order3','BLUE-LIPSTICK',14),
    (4,'order4','DECORATIVE-WIDGET',12)
"""
