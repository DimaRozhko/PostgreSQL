from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from entity.Departament import Departament
from entity.Order import Order
from entity.Person import Person
from entity.Thing import Thing
from entity.Type import Type


class ProcessORM(object):

    # Constructor
    def __init__(self):
        self.__engine = create_engine("postgresql://postgres:2000@localhost:5432/store")
        self.__Session = sessionmaker(bind=self.__engine)
        self.session = self.__Session()

    def __del__(self):
        self.session.close()

    def add_departament(self, departanemt_id, name, country):
        self.session.add(Departament(departanemt_id, name, country))
        self.session.commit()

    def delete_departament_by_id(self, departaments_id):
        self.session.query(Departament).filter_by(departaments_id=departaments_id).delete()
        self.session.commit()

    def update_departament_name_by_id(self, departaments_id, new_name):
        self.session.query(Departament).filter_by(departaments_id=departaments_id).update({'name': new_name})
        self.session.commit()

    def add_order(self, order_id, quantity, date, person_id):
        self.session.add(Order(order_id, quantity, date, person_id))
        self.session.commit()

    def delete_order_by_id(self, order_id):
        self.session.query(Order).filter_by(order_id=order_id).delete()
        self.session.commit()

    def update_order_quantity_by_id(self, order_id, new_quantity):
        self.session.query(Order).filter_by(order_id=order_id).update({'quantity': new_quantity})
        self.session.commit()

    def add_person(self, person_id, name, address, email, tel_num):
        self.session.add(Person(person_id, name, address, email, tel_num))
        self.session.commit()

    def delete_person_by_id(self, person_id):
        self.session.query(Person).filter_by(person_id=person_id).delete()
        self.session.commit()

    def update_person_email_by_id(self, person_id, new_email):
        self.session.query(Person).filter_by(person_id=person_id).update({'contact_email': new_email})
        self.session.commit()

    def add_thing(self, thing_id, quantity, expiration_date, breakable, type_id, order_id, name):
        self.session.add(Thing(thing_id, quantity, expiration_date, breakable, type_id, order_id, name))
        self.session.commit()

    def delete_thing_by_id(self, thing_id):
        self.session.query(Thing).filter_by(thing_id=thing_id).delete()
        self.session.commit()

    def update_thing_quantity_by_id(self, thing_id, new_quantity):
        self.session.query(Thing).filter_by(thing_id=thing_id).update({'quantity': new_quantity})
        self.session.commit()

    def add_type(self, type_id, spoil_quick, type_name):
        self.session.add(Type(type_id, spoil_quick, type_name))
        self.session.commit()

    def delete_type_by_id(self, type_id):
        self.session.query(Person).filter_by(type_id=type_id).delete()
        self.session.commit()

    def update_type_name_by_id(self, type_id, new_type_name):
        self.session.query(Person).filter_by(type_id=type_id).update({'type_name': new_type_name})
        self.session.commit()


