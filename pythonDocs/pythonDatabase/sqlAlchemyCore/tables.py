from sqlalchemy import Table, MetaData, Column
from sqlalchemy import Integer, String, Text, ForeignKey
"""
users table:
      - id primary key
      - name String
      - fullname String
      - email


comment table:
        - id primary key
        - comment String
        - user_id int > users.id
"""


meta_obj = MetaData()


users_table = Table(
    "users",
    meta_obj,
    Column("id",Integer,primary_key=True),
    Column("name",String(25),nullable=False),
    Column("fullname",Text)

)

comments_table = Table(
    "comments",
    meta_obj,
    Column("id",Integer,primary_key=True),
    Column("comment",Text(),nullable=False),
    Column("user_id",ForeignKey("users.id"))
)