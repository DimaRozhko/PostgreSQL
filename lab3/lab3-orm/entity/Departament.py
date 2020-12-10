from entity.BaseDeclare import Base
from sqlalchemy import Column, Integer, Text


class Departament(Base):

    __tablename__ = 'departament'
    departaments_id = Column(Integer, primary_key=True, nullable=False)
    name = Column('name', Text)
    country = Column('country', Text)

    def __init__(self, departanemt_id, name, country):
        self.departaments_id = departanemt_id
        self.name = name
        self.country = country
