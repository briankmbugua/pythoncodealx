from tables import users_table
from connect import engine
from sqlalchemy import select


statement = select(users_table).where(users_table.c.name == "kim")

with engine.connect() as conn:
    result = conn.execute(statement)

    for row in result:
        print(f"<Username= {row.name} fullname={row.fullname}")


print(statement)

# print(users_table.c.name)
# print(users_table.c.fullname)
# print(users_table.c.id)