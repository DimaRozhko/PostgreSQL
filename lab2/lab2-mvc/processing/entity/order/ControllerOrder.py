from processing.basic import ExceptionsMVC as mvc_exc
from processing.basic.ControllerBasic import ControllerBasic
from processing.entity.order.ModelOrder import ModelOrder
import datetime
from datetime import datetime as datestr


class ControllerOrder(ControllerBasic):

    def __init__(self, view):
        super(ControllerOrder, self).__init__(ModelOrder(), view)

    def validation(self, order_id, quantity, date, person_id):
        assert order_id > 0, '\'order_id\' must be greater than 0'
        assert quantity > 0, '\'quantity\' must be greater than 0'
        assert person_id > 0, '\'person_id\' must be greater than 0'
        assert isinstance(order_id, int), '\'order_id\' must be \'int\' type'
        assert isinstance(quantity, int), '\'quantity\' must be \'int\' type'
        assert isinstance(date, datetime.date), '\'date\' must be \'date\' type'
        assert isinstance(person_id, int), '\'person_id\' must be \'int\' type'

    def insert_item(self, list_atr):
        order_id = list_atr[0]
        quantity = list_atr[1]
        date = datestr.strptime(list_atr[2], '%d/%m/%Y')
        person_id = list_atr[3]
        self.validation(order_id, quantity, date, person_id)
        item_type = self.model.item_type
        try:
            self.model.create_item(order_id, quantity, date, person_id)
            self.view.display_item_stored(list_atr, "ORDER")
        except mvc_exc.ItemAlreadyStored as e:
            self.view.display_item_already_stored_error(list_atr, order_id, e)

    def update_item(self, target, list_atr):
        order_id = list_atr[0]
        quantity = list_atr[1]
        date = datestr.strptime(list_atr[2], '%d/%m/%Y')
        person_id = list_atr[3]
        self.validation(order_id, quantity, date, person_id)
        item_type = self.model.item_type
        try:
            # older = self.model.read_item(target, name)
            self.model.update_item(target, order_id, quantity, date, person_id)
            # self.view.display_item_updated(
            #     name, older['price'], older['quantity'], price, quantity)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(order_id, item_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

