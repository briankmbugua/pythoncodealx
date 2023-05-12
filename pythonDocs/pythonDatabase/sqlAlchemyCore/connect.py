from sqlalchemy import create_engine, text

engine = create_engine("mysql+pymysql://root:password@127.0.0.1:3306/sqlAlchemyCore", echo=True)

# with engine.connect() as conn:
#     stmt = text('SELECT "hello"')
#     result = conn.execute(stmt)
#     print(result.all())