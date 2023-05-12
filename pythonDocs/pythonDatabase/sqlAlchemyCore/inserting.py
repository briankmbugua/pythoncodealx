from sqlalchemy import insert
from tables import users_table
from connect import engine

statement = insert(users_table)

with engine.connect() as conn:
    conn.execute(statement,[
        {"name":"kim","fullname":"edgar kimani"},
        {"name":"susan","fullname":"susan muthoni"},
        {"name":"oscar","fullname":"oscar njenga"}
    ])
    conn.commit()
print(statement)
