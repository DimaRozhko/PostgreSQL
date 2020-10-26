from processing.basic.ModelBasic import ModelBasic
from processing.entity.thing.ItemThing import ItemThing


class ModelThing(ModelBasic):

    def __init__(self):
        super(ModelThing, self).__init__("thing", item=ItemThing())

    def create_item(self, thing_id, quantity, expiration_date, breakable, type_id, order_id, name):
        self.item.create_item(thing_id, quantity, expiration_date, breakable, type_id, order_id, name)
        # print(self.item.get_items())

    def read_item(self, column, data):
        return self.item.read_item(column, data)

    def update_item(self, target, thing_id, quantity, expiration_date, breakable, type_id, order_id, name):
        self.item.update_item(target, thing_id, quantity, expiration_date, breakable, type_id, order_id, name)

    def delete_item(self, column, val):
        self.item.delete_item(column, val)
