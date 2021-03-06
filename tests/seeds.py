CREATE_ORDER_LINES_TABLE = """
DROP TABLE IF EXISTS "order_lines";
CREATE TABLE IF NOT EXISTS "order_lines" (
    id SERIAL,
    order_id varchar(255),
    sku varchar(255),
    qty int4,
    CONSTRAINT "order_lines_pkey" PRIMARY KEY (id)
);
"""

ORDER_LINES_SEED = """
INSERT INTO
    "order_lines" (id, order_id, sku, qty)
VALUES
    (1,'order1','RED-CHAIR',12),
    (2,'order2','RED-TABLE',13),
    (3,'order3','BLUE-LIPSTICK',14),
    (4,'order4','GENERIC-SOFA',12)
"""

CREATE_BATCHES_TABLE = """
DROP TABLE IF EXISTS "batches";
CREATE TABLE IF NOT EXISTS "batches" (
    id SERIAL,
    reference varchar(255),
    sku varchar(255),
    _purchased_quantity int4,
    eta date,
    CONSTRAINT "batches_pkey" PRIMARY KEY (id)
);
"""

BATCHES_SEED = """
INSERT INTO
    "batches" (id, reference, sku, _purchased_quantity, eta)
VALUES
    (1,'batch1','RUSTY-SOAPDISH',100,Null)
"""
