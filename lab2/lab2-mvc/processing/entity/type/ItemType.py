from processing.basic import ExceptionsMVC as mvc_exc
from processing.basic.ItemBasic import ItemBasic
from entity.Type import Type


class ItemType(ItemBasic):

    def __init__(self):
        super(ItemType, self).__init__()

    def create_item(self, type_id, spoil_quick, type_name):
        results = []
        for row in self.items:
            if len(row) != 0:
                if row['type_id'] == type_id:
                    results.append(row['type_id'])
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(type_id))
        else:
            results = Type().generator(list([type_id, spoil_quick, type_name]))
            self.items.append(results)
            self.db.execute_query(f"INSERT INTO {self.table_name} "
                                  f"    (type_id, spoil_quick, type_name) "
                                  f"VALUES ({results['type_id']}, {results['spoil_quick']}, "
                                  f"'{(results['type_name'])}');")

    def update_item(self, target, type_id, spoil_quick, type_name):
        i = []
        tar = type_id if (target == 'type_id') \
            else spoil_quick if (target == 'spoil_quick') \
            else type_name if (target == 'type_name') \
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
                    self.items[idx] = Type().\
                        generator(list([type_id, spoil_quick, type_name]))
                    self.db.update_table(self.table_name,
                                         f"type_id={self.items[idx]['type_id']}, "
                                         f"spoil_quick={self.items[idx]['spoil_quick']}, "
                                         f"type_name='{self.items[idx]['type_name']}', ",
                                         target + "=" + str(tar))
                # print(self.items)
            else:
                raise mvc_exc.ItemNotStored(
                    'Can\'t update "{}" because it\'s not stored'.format(tar))


