from processing.basic.ItemBasic import ItemBasic


class ModelBasic(object):

    def __init__(self, entity_name, item=ItemBasic()):
        self._item_type = entity_name
        self.item = item
        self.create_items_by_table_name(entity_name)

    def get_item(self):
        return self.item.get_items()

    @property
    def item_type(self):
        return self._item_type

    @item_type.setter
    def item_type(self, new_item_type):
        self._item_type = new_item_type

    def create_items(self, items):
        self.item.create_items(items)

    def create_items_by_table_name(self, items):
        self.item.create_items_by_table_name(items)

    def read_items(self):
        return self.item.read_items()

    def generate_random(self, num):
        self.item.random_generate(num)

    def find(self):
        self.item.find()

    def delete_item(self, column, val):
        return self.item.delete_item(column, val)

    def read_item(self, column, data):
        return self.item.read_item(column, data)