from processing.basic import ExceptionsMVC as mvc_exc
from processing.basic.ProcessDB import ProcessDB


class ItemBasic(object):

    def __init__(self):
        self.db = ProcessDB()
        self.items = list()
        self.table_name = ""

    def get_items(self):
        return self.items

    def random_generate(self, num):
        self.db.random_generate_and_print(num)

    def create_items_by_table_name(self, table_name):
        self.table_name = table_name
        self.db.set_listTable_by_db(table_name)
        self.items = self.db.get_list_table()

    def create_items(self, app_items):
        self.items = app_items

    def read_item(self, column, data):
        myitems = []
        for row in self.items:
            if len(row) != 0:
                if row[column] == data:
                    myitems.append(row[column])
        if myitems:
            return myitems[0]
        else:
            raise mvc_exc.ItemNotStored(
                'Can\'t read "{}" because it\'s not stored'.format(data))

    def read_items(self):
        return [self.item for self.item in self.items]

    def find(self):
        self.db.find_in_table(self.table_name)

    def delete_item(self, column, val):
        idxs_items = []
        for row in self.items:
            if len(row) != 0:
                if row[column] == val:
                    idxs_items.append(row[column])
                    break
        if idxs_items:
            idxs_items = []
            for row in self.items:
                if len(row) != 0:
                    if row[column] != val:
                        idxs_items.append(row)
            del self.items
            self.items = idxs_items
            self.db.del_row_in_table(self.table_name, str(column) + "=" + str(val))
        else:
            raise mvc_exc.ItemNotStored(
                'Can\'t delete "{}" because it\'s not stored'.format(val))

