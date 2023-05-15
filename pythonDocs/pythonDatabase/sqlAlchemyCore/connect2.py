from sqlalchemy import create_engine, text

#create an engine for connection
engine = create_engine('pymsql+mysql://root:password@127.0.0.1:3306/dbone', echo = True);

with engine.connect() as conn:
    statement = text("SELECT 'HELLO' ")
    result = conn.execute(statement)
    print(result.all())
