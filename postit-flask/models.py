import sqlalchemy
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Integer, Column, String

engine = sqlalchemy.create_engine('mariadb+mariadbconnector://root:V2DAxA@127.0.0.1:3306/postit')

Base = declarative_base()

class Note(Base):
    __tablename__ = 'notes'
    id = Column(Integer, primary_key=True, autoincrement=True)
    text = Column(String(length=500))

Base.metadata.create_all(engine)
Session = sqlalchemy.orm.sessionmaker()
Session.configure(bind=engine)
session = Session()
