from processing.basic import ExceptionsMVC as mvc_exc
from processing.basic.ItemBasic import ItemBasic
from entity.Person import Person


class ItemPerson(ItemBasic):

    def __init__(self):
        super(ItemPerson, self).__init__()

    def create_item(self, person_id, name, address, contact_email, contact_tel_num):
        results = []
        for row in self.items:
            if len(row) != 0:
                if row['person_id'] == person_id:
                    results.append(row['person_id'])
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(person_id))
        else:
            results = Person().generator(list([person_id, name, address, contact_email, contact_tel_num]))
            self.items.append(results)
            self.db.execute_query(f"INSERT INTO {self.table_name} "
                                  f"    (person_id, name, address, contact_email, contact_tel_num) "
                                  f"VALUES ({results['person_id']}, '{results['name']}', "
                                  f"'{(results['address'])}', '{results['contact_email']}',"
                                  f"'{results['contact_tel_num']}');")

    def update_item(self, target, person_id, name, address, contact_email, contact_tel_num):
        i = []
        tar = person_id if (target == 'person_id') \
            else name if (target == 'name') \
            else address if (target == 'address') \
            else contact_email if (target == 'contact_email') \
            else contact_tel_num if (target == 'contact_tel_num') \
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
                    self.items[idx] = Person().\
                        generator(list([person_id, name, address, contact_email, contact_tel_num]))
                    self.db.update_table(self.table_name,
                                         f"person_id={self.items[idx]['person_id']}, "
                                         f"name='{self.items[idx]['name']}', "
                                         f"address='{self.items[idx]['address']}', "
                                         f"contact_email='{self.items[idx]['contact_email']}', "
                                         f"contact_tel_num='{self.items[idx]['contact_tel_num']}', ",
                                         target + "=" + str(tar))
                # print(self.items)
            else:
                raise mvc_exc.ItemNotStored(
                    'Can\'t update "{}" because it\'s not stored'.format(tar))


