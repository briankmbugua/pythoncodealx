from tables import users_table
from connect import engine
from sqlalchemy import delete

statement = delete(users_table).where(
    users_table.c.name == "kimani"
)


with engine.connect() as conn:
    conn.execute(statement)
    conn.commit()