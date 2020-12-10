from entity.BaseDeclare import Base
from sqlalchemy import Column, Integer, Text


class Person(Base):

    __tablename__ = 'person'
    person_id = Column(Integer, primary_key=True, nullable=False)
    name = Column('name', Text)
    address = Column('address', Text)
    contact_email = Column('contact_email', Text)
    contact_tel_num = Column('contact_tel_num', Text)

    def __init__(self, person_id, name, address, email, tel_num):
        self.person_id = person_id
        self.name = name
        self.address = address
        self.contact_email = email
        self.contact_tel_num = tel_num
