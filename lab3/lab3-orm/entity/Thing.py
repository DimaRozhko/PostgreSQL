from entity.BaseDeclare import Base
from sqlalchemy import Column, Integer, Text, Date, Boolean
from sqlalchemy import ForeignKey

class Thing(Base):

    __tablename__ = 'thing'
    thing_id = Column(Integer, primary_key=True, nullable=False)
    quantity = Column('quantity', Integer)
    expiration_date = Column('expiration_date', Date)
    breakable = Column('breakable', Boolean)
    type_id = Column('type_id', Integer, ForeignKey('type.type_id'))
    order_id = Column('order_id', Integer, ForeignKey('order.order_id'))
    name = Column('name', Text)

    def __init__(self, thing_id, quantity, expiration_date, breakable, type_id, order_id, name):
        self.thing_id = thing_id
        self.quantity = quantity
        self.expiration_date = expiration_date
        self.breakable = breakable
        self.type_id = type_id
        self.order_id = order_id
        self.name = name
