from processing.basic import ExceptionsMVC as mvc_exc
from processing.basic.ControllerBasic import ControllerBasic
from processing.entity.person.ModelPerson import ModelPerson


class ControllerPerson(ControllerBasic):

    def __init__(self, view):
        super(ControllerPerson, self).__init__(ModelPerson(), view)

    def validation(self, person_id, name, address, contact_email, contact_tel_num):
        assert person_id > 0, '\'person_id\' must be greater than 0'
        assert isinstance(name, str), '\'name\' must be \'string\' type'
        assert isinstance(address, str), '\'address\' must be \'string\' type'
        assert isinstance(contact_email, str), '\'contact_email\' must be \'string\' type'
        assert isinstance(contact_tel_num, str), '\'contact_tel_num\' must be \'string\' type'

    def insert_item(self, list_atr):
        person_id = list_atr[0]
        name = list_atr[1]
        address = list_atr[2]
        contact_email = list_atr[3]
        contact_tel_num = list_atr[4]
        self.validation(person_id, name, address, contact_email, contact_tel_num)
        # print(breakable)
        # print(name)
        item_type = self.model.item_type
        print(item_type)
        try:
            self.model.create_item(person_id, name, address, contact_email, contact_tel_num)
            self.view.display_item_stored(person_id, name, address, contact_email, contact_tel_num)

        except mvc_exc.ItemAlreadyStored as e:
            self.view.display_item_already_stored_error(person_id, item_type, e)

    def update_item(self, target, list_atr):
        person_id = list_atr[0]
        name = list_atr[1]
        address = list_atr[2]
        contact_email = list_atr[3]
        contact_tel_num = list_atr[4]
        self.validation(person_id, name, address, contact_email, contact_tel_num)
        item_type = self.model.item_type
        try:
            # older = self.model.read_item(target, name)
            self.model.update_item(target, person_id, name, address, contact_email, contact_tel_num)
            # self.view.display_item_updated(
            #     name, older['price'], older['quantity'], price, quantity)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(person_id, item_type, e)
            # if the item is not yet stored and we performed an update, we have
            # 2 options: do nothing or call insert_item to add it.
            # self.insert_item(name, price, quantity)

