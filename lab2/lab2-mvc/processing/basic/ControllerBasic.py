from processing.basic import ExceptionsMVC as mvc_exc
import datetime


class ControllerBasic(object):

    def __init__(self, model, view):
        self.model = model
        self.view = view

    def get_item(self):
        return self.model.get_item()

    def get_table_name(self):
        return self.model.item_type

    def get_list_input(self, table_name, attribute):
        list_input = []
        print(f"TABLE if date use format dd/mm/yyyy \'{table_name}\'")
        for column in attribute:
            print(f"Input '{column}':")
            inp = input()
            if inp.isdigit():
                inp = int(inp)
                print("INT")
            list_input.append(inp)
        return list_input

    def show_items(self, bullet_points=False):
        items = self.model.read_items()
        item_type = self.model.item_type
        if bullet_points:
            self.view.show_bullet_point_list(item_type, items)
        else:
            self.view.show_number_point_list(item_type, items)

    def show_item(self, item_column, item_data):
        try:
            item = self.model.read_item(item_column, item_data)
            item_type = self.model.item_type
            self.view.show_item(item_type, item_data, item)
        except mvc_exc.ItemNotStored as e:
            self.view.display_missing_item_error(item_data, e)

    def generate_random(self, num):
        self.model.generate_random(num)

    def find(self):
        self.model.find()

    def delete_item(self, column, val):
        item_type = self.model.item_type
        try:
            self.model.delete_item(column, val)
            self.view.display_item_deletion(id)
        except mvc_exc.ItemNotStored as e:
            self.view.display_item_not_yet_stored_error(val, item_type, e)