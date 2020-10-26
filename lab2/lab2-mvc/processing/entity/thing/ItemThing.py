from processing.basic import ExceptionsMVC as mvc_exc
from processing.basic.ItemBasic import ItemBasic
from entity.Thing import Thing

class ItemThing(ItemBasic):

    def __init__(self):
        super(ItemThing, self).__init__()


    def create_item(self, thing_id, quantity, expiration_date, breakable, type_id, order_id, name):
        results = []
        for row in self.items:
            if len(row) != 0:
                if row['thing_id'] == thing_id:
                    results.append(row['thing_id'])
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(name))
        else:
            results = Thing().generator(list([thing_id, quantity, expiration_date,
                                              breakable, type_id, order_id, name]))
            self.items.append(results)
            self.db.execute_query(f"INSERT INTO {self.table_name} "
                                  f"    (thing_id, quantity, expiration_date, breakable, type_id, order_id, name) "
                                  f"VALUES ({results['thing_id']}, {results['quantity']}, "
                                  f"'{(results['expiration_date'])}', {results['breakable']}, "
                                  f"{results['type_id']}, {results['order_id']}, "
                                  f"'{results['name']}');")

    def update_item(self, target, thing_id, quantity, expiration_date, breakable, type_id, order_id, name):
        i = []
        tar = thing_id if (target == 'thing_id') \
            else quantity if (target == 'quantity') \
            else expiration_date if (target == 'expiration_date') \
            else breakable if (target == 'breakable') \
            else type_id if (target == 'type_id') \
            else order_id if (target == 'order_id') \
            else name if (target == 'name')\
            else None
        if tar is not None:
            j = 0
            for row in self.items:
                if len(row) != 0:
                    if row[target] == tar:
                        i.append(j)
                j += 1
            if i:
                for idx in i:
                    self.items[idx] = Thing().generator(list([thing_id, quantity, expiration_date,
                                                              breakable, type_id, order_id, name]))
                    self.db.update_table(self.table_name,
                                        f"thing_id={self.items[idx]['thing_id']}, "
                                        f"quantity={self.items[idx]['quantity']}, "
                                        f"expiration_date='{self.items[idx]['expiration_date']}', "
                                        f"breakable={self.items[idx]['breakable']}, "
                                        f"type_id={self.items[idx]['type_id']}, "
                                        f"order_id={self.items[idx]['order_id']}, "
                                        f"name='{self.items[idx]['name']}'",
                                         target + "=" + str(tar))
                # print(self.items)
            else:
                raise mvc_exc.ItemNotStored(
                    'Can\'t update "{}" because it\'s not stored'.format(tar))

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