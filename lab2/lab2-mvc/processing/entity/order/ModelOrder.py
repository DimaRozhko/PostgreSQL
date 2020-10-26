from processing.basic.ModelBasic import ModelBasic
from processing.entity.order.ItemOrder import ItemOrder


class ModelOrder(ModelBasic):

    def __init__(self):
        super(ModelOrder, self).__init__("public.order", item=ItemOrder())

    def create_item(self, order_id, quantity, date, person_id):
        self.item.create_item(order_id, quantity, date, person_id)
        # print(self.item.get_items())

    def update_item(self, target, order_id, quantity, date, person_id):
        self.item.update_item(target, order_id, quantity, date, person_id)


