from sqlalchemy import create_engine, inspect
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, Session, relationship
from sqlalchemy import Column, Integer, Text


SQL_URI = r"sqlite:///models02.db"

Base = declarative_base()
engine = create_engine(SQL_URI, echo = False)
Session = sessionmaker(bind = engine)
sess = Session()


class Apple_health_export(Base):
    __tablename__ = 'apple_health_export'
    id = Column(Integer,primary_key = True)
    creationDate = Column(Text)
    value = Column(Text)


    def __repr__(self):
        return f'Apple_health_export(id: {self.id},'  \
            f'creationDate: {self.creationDate})'

#Build db
if 'users' in inspect(engine).get_table_names():
    print('db already exists')
else:
    Base.metadata.create_all(engine)
    print('NEW db created.')



