from processing.basic import ExceptionsMVC as mvc_exc
from processing.basic.ItemBasic import ItemBasic
from entity.Departament import Departament


class ItemDepartament(ItemBasic):

    def __init__(self):
        super(ItemDepartament, self).__init__()

    def create_item(self, departament_id, name, country):
        results = []
        for row in self.items:
            if len(row) != 0:
                if row['departament_id'] == departament_id:
                    results.append(row['departament_id'])
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(name))
        else:
            results = Departament().generator(list([departament_id, name, country]))
            self.items.append(results)
            self.db.execute_query(f"INSERT INTO {self.table_name} "
                                  f"    (departament_id, name, country) "
                                  f"VALUES ({results['departament_id']}, '{results['name']}', "
                                  f"'{(results['country'])}');")

    def update_item(self, target, departament_id, name, country):
        i = []
        tar = departament_id if (target == 'departament_id') \
            else name if (target == 'name') \
            else country if (target == 'country') \
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
                    self.items[idx] = Departament().generator(list([departament_id, name, country]))
                    self.db.update_table(self.table_name,
                                         f"departament_id={self.items[idx]['departament_id']}, "
                                         f"name='{self.items[idx]['name']}', "
                                         f"country='{self.items[idx]['country']}' ",
                                         target + "=" + str(tar))
                # print(self.items)
            else:
                raise mvc_exc.ItemNotStored(
                    'Can\'t update "{}" because it\'s not stored'.format(tar))


