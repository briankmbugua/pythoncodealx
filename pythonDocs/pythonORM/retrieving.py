from main import User, Session, engine

#create a local session class
local_session = Session(bind=engine)


#returns all objects
# users=local_session.query(User).all()

#filter to return some objects
# users = local_session.query(User).all()[:3]
# for user in users:
#     print(user.username)

#return one specific user object

jona = local_session.query(User).filter(User.username=="jona").first()
print(jona)
