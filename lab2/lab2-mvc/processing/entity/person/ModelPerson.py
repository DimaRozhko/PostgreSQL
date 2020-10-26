from processing.basic.ModelBasic import ModelBasic
from processing.entity.person.ItemPerson import ItemPerson


class ModelPerson(ModelBasic):

    def __init__(self):
        super(ModelPerson, self).__init__("person", item=ItemPerson())

    def create_item(self, person_id, name, address, contact_email, contact_tel_num):
        self.item.create_item(person_id, name, address, contact_email, contact_tel_num)
        # print(self.item.get_items())

    def update_item(self, target, person_id, name, address, contact_email, contact_tel_num):
        self.item.update_item(target, person_id, name, address, contact_email, contact_tel_num)


