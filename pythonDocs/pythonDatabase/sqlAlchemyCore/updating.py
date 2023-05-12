from tables import users_table
from connect import engine
from sqlalchemy import update

statement = update(users_table).where(
    users_table.c.name == "kim"
).values(name="kimani")

with engine.connect() as conn:
    conn.execute(statement)
    conn.commit()