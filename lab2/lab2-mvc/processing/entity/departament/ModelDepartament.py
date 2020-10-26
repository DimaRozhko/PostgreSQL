from processing.basic.ModelBasic import ModelBasic
from processing.entity.departament.ItemDepartament import ItemDepartament


class ModelDepartament(ModelBasic):

    def __init__(self):
        super(ModelDepartament, self).__init__("departament", item=ItemDepartament())

    def create_item(self, departament_id, name, country):
        self.item.create_item(departament_id, name, country)
        # print(self.item.get_items())

    def update_item(self, target, departament_id, name, country):
        self.item.update_item(target, departament_id, name, country)


