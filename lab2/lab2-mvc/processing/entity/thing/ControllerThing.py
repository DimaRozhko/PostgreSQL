from processing.basic import ExceptionsMVC as mvc_exc
from processing.basic.ControllerBasic import ControllerBasic
from processing.entity.thing.ModelThing import ModelThing
from datetime import datetime as date
import datetime


class ControllerThing(ControllerBasic):

    def __init__(self, view):
        super(ControllerThing, self).__init__(ModelThing(), view)

    def validation(self, thing_id, quantity, expiration_date, breakable, type_id, order_id, name):
        assert thing_id > 0, '\'thing_id\' must be greater than 0'
        assert quantity >= 0, '\'quantity\' must be greater than or equal to 0'
        assert type_id > 0, '\'type_id\' must be greater than 0'
        assert order_id > 0, '\'order_id\' must be greater than 0'
        assert isinstance(thing_id, int), '\'thing_id\' must be \'int\' type'
        assert isinstance(quantity, int), '\'quantity\' must be \'int\' type'
        assert isinstance(expiration_date, datetime.date), '\'expiration date\' must be \'date\' type'
        assert isinstance(breakable, bool), '\'breakable\' must be \'bool\' type'
        assert isinstance(type_id, int), '\'type_id\' must be \'int\' type'
        assert isinstance(order_id, int), '\'order_id\' must be \'int\' type'
        assert isinstance(name, str), '\'name\' must be \'string\' type'

    def insert_item(self, list_atr):
        thing_id = list_atr[0]
        quantity = list_atr[1]
        expiration_date = date.strptime(list_atr[2], '%d/%m/%Y')
        breakable = eval(list_atr[3])
        type_id = list_atr[4]
        order_id = list_atr[5]
        name = list_atr[6]
        self.validation(thing_id, quantity, expiration_date, breakable, type_id, order_id, name)
        # print(breakable)
        # print(name)
        item_type = self.model.item_type
        print(item_type)
        try:
            self.model.create_item(thing_id, quantity, expiration_date, breakable, type_id, order_id, name)
            self.view.display_item_stored(thing_id, quantity, expiration_date, breakable, type_id, order_id, name)

        except mvc_exc.ItemAlreadyStored as e:
            self.view.display_item_already_stored_error(name, item_type, e)

    def update_item(self, target, list_atr):
        thing_id = list_atr[0]
        quantity = list_atr[1]
        expiration_date = date.strptime(list_atr[2], '%d/%m/%Y')
        breakable = eval(list_atr[3])
        type_id = list_atr[4]
        order_id = list_atr[5]
        name = list_atr[6]
        self.validation(thing_id, quantity, expiration_date, breakable, type_id, order_id, name)
        item_type = self.model.item_type
        try:
            # older = self.model.read_item(target, name)
            self.model.update_item(target, thing_id, quantity, expiration_date, breakable, type_id, order_id, name)
            # self.view.display_item_updated(
            #     name, older['price'], older['quantity'], price, quantity)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(name, item_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

    def update_item_type(self, new_item_type):
        old_item_type = self.model.item_type
        self.model.item_type = new_item_type
        self.view.display_change_item_type(old_item_type, new_item_type)
