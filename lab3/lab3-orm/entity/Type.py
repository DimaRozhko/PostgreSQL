from entity.BaseDeclare import Base
from sqlalchemy import Column, Integer, Text, Boolean


class Type(Base):

    __tablename__ = 'type'
    type_id = Column(Integer, primary_key=True, nullable=False)
    spoil_quick = Column('spoil_quick', Boolean)
    type_name = Column('type_name', Text)

    def __init__(self, type_id, spoil_quick, type_name):
        self.type_id = type_id
        self.spoil_quick = spoil_quick
        self.type_name = type_name
