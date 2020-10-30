from processing.basic import ExceptionsMVC as mvc_exc
from processing.basic.ControllerBasic import ControllerBasic
from processing.entity.type.ModelType import ModelType


class ControllerType(ControllerBasic):

    def __init__(self, view):
        super(ControllerType, self).__init__(ModelType(), view)

    def validation(self, type_id, spoil_quick, type_name):
        assert type_id > 0, '\'type_id\' must be greater than 0'
        assert isinstance(type_id, int), '\'type_id\' must be \'integer\' type'
        assert isinstance(spoil_quick, bool), '\'spoil_quick\' must be \'boolean\' type'
        assert isinstance(type_name, str), '\'type_name\' must be \'string\' type'

    def insert_item(self, list_atr):
        type_id = list_atr[0]
        spoil_quick = eval(list_atr[1])
        type_name = list_atr[2]
        self.validation(type_id, spoil_quick, type_name)
        item_type = self.model.item_type
        try:
            self.model.create_item(type_id, spoil_quick, type_name)
            self.view.display_item_stored(list_atr, "TYPE")
        except mvc_exc.ItemAlreadyStored as e:
            self.view.display_item_already_stored_error(list_atr, type_name, e)

    def update_item(self, target, list_atr):
        type_id = list_atr[0]
        spoil_quick = list_atr[1]
        type_name = list_atr[2]
        self.validation(type_id, spoil_quick, type_name)
        item_type = self.model.item_type
        try:
            # older = self.model.read_item(target, name)
            self.model.update_item(target, type_id, spoil_quick, type_name)
            # self.view.display_item_updated(
            #     name, older['price'], older['quantity'], price, quantity)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(type_id, item_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

