from main import Session, engine, User
from sqlalchemy import desc

local_session = Session(bind=engine)

# #asceding
# users=local_session.query(User).order_by(User.username).all()
#descending
users_desc=local_session.query(User).order_by(desc(User.username)).all()
for user in users_desc:
    print(f"User {user.username}")
