from processing.basic.ModelBasic import ModelBasic
from processing.entity.type.ItemType import ItemType


class ModelType(ModelBasic):

    def __init__(self):
        super(ModelType, self).__init__("type", item=ItemType())

    def create_item(self, type_id, spoil_quick, type_name):
        self.item.create_item(type_id, spoil_quick, type_name)
        # print(self.item.get_items())

    def update_item(self, target, type_id, spoil_quick, type_name):
        self.item.update_item(target, type_id, spoil_quick, type_name)


