from main import User,Session, engine



users = [
    {
        "username":"brian",
        "email":"brina@mail.com"
    },
        {
        "username":"pauline",
        "email":"pauline@mail.com"
    },
        {
        "username":"kimani",
        "email":"kimani@mail.com"
    },
        {
        "username":"edgar",
        "email":"edgar@mail.com"
    }
    
]

local_session = Session(bind=engine)

# new_user=User(username="jona", email="jona@mail.com")

# local_session.add(new_user)

# local_session.commit()

for u in users:
    new_user=User(username=u["username"], email=u["email"])
    local_session.add(new_user)
    local_session.commit()
    print(f"added {u['username']}")