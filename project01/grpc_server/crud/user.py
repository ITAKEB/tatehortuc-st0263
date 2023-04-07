from crud.connection import engine, Base, Session

from datetime import datetime
from sqlalchemy import Column, String, DateTime, select
from sqlalchemy.dialects.postgresql import UUID

class User(Base):
    __tablename__ = 'users'

    id = Column(UUID(), primary_key=True)
    username = Column(String(50), nullable=False, unique=True)
    password = Column(String(50), nullable=False)
    created_at = Column(DateTime(), default=datetime.now())


    def __str__(self):
        return self.username


session = Session()
Base.metadata.create_all(engine)

# insert into users (id, username, password) values ($id, $username, $password);
def save_user(uuid, username, password):
    new_user = User(id=uuid, username=username, password=password) 
    session.add(new_user)

    session.commit()


# select * from users where username = $username and password = $password;
def get_user(username, password):
    select = session.query(User.id).filter(
        User.username == username
    ).filter(
        User.password == password
    )
        
    for row in select:
        if (row):
            #extract uuid from sql tuple response
            uuid = row[0]
            return uuid

    return None

