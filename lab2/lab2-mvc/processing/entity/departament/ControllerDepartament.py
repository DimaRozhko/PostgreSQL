from processing.basic import ExceptionsMVC as mvc_exc
from processing.basic.ControllerBasic import ControllerBasic
from processing.entity.departament.ModelDepartament import ModelDepartament


class ControllerDepartament(ControllerBasic):

    def __init__(self, view):
        super(ControllerDepartament, self).__init__(ModelDepartament(), view)

    def validation(self, departament_id, name, country):
        assert departament_id > 0, '\'departament_id\' must be greater than 0'
        assert isinstance(departament_id, int), '\'departament_id\' must be \'int\' type'
        assert isinstance(name, str), '\'name\' must be \'string\' type'
        assert isinstance(country, str), '\'country\' must be \'string\' type'

    def insert_item(self, list_atr):
        departament_id = list_atr[0]
        name = list_atr[1]
        country = list_atr[2]
        self.validation(departament_id, name, country)
        # print(breakable)
        # print(name)
        item_type = self.model.item_type
        print(item_type)
        try:
            self.model.create_item(departament_id, name, country)
            self.view.display_item_stored(departament_id, name, country)

        except mvc_exc.ItemAlreadyStored as e:
            self.view.display_item_already_stored_error(name, item_type, e)

    def update_item(self, target, list_atr):
        departament_id = list_atr[0]
        name = list_atr[1]
        country = list_atr[2]
        self.validation(departament_id, name, country)
        item_type = self.model.item_type
        try:
            # older = self.model.read_item(target, name)
            self.model.update_item(target, departament_id, name, country)
            # self.view.display_item_updated(
            #     name, older['price'], older['quantity'], price, quantity)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(name, item_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

