from entity.BaseDeclare import Base
from sqlalchemy import Column, Integer, Date
from sqlalchemy import ForeignKey

class Order(Base):

    __tablename__ = 'order'
    order_id = Column(Integer, primary_key=True, nullable=False)
    quantity = Column('quantity', Integer)
    date = Column('date', Date)
    person_id = Column('person_id', Integer, ForeignKey('person.person_id'))

    def __init__(self, order_id, quantity, date, person_id):
        self.order_id = order_id
        self.quantity = quantity
        self.date = date
        self.person_id = person_id
