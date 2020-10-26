from processing.basic import ExceptionsMVC as mvc_exc
from processing.basic.ItemBasic import ItemBasic
from entity.Order import Order


class ItemOrder(ItemBasic):

    def __init__(self):
        super(ItemOrder, self).__init__()

    def create_item(self, order_id, quantity, date, person_id):
        results = []
        for row in self.items:
            if len(row) != 0:
                if row['order_id'] == order_id:
                    results.append(row['order_id'])
        if results:
            raise mvc_exc.ItemAlreadyStored('"{}" already stored!'.format(order_id))
        else:
            results = Order().generator(list([order_id, quantity, date, person_id]))
            self.items.append(results)
            self.db.execute_query(f"INSERT INTO {self.table_name} "
                                  f"    (order_id, quantity, date, person_id) "
                                  f"VALUES ({results['order_id']}, {results['quantity']}, "
                                  f"'{(results['date'])}', {results['person_id']});")

    def update_item(self, target, order_id, quantity, date, person_id):
        i = []
        tar = order_id if (target == 'order_id') \
            else quantity if (target == 'quantity') \
            else date if (target == 'date') \
            else person_id if (target == 'person_id') \
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
                    self.items[idx] = Order().\
                        generator(list([order_id, quantity, date, person_id]))
                    self.db.update_table(self.table_name,
                                         f"order_id={self.items[idx]['order_id']}, "
                                         f"quantity={self.items[idx]['quantity']}, "
                                         f"date='{self.items[idx]['date']}', "
                                         f"person_id={self.items[idx]['person_id']} ",
                                         target + "=" + str(tar))
                # print(self.items)
            else:
                raise mvc_exc.ItemNotStored(
                    'Can\'t update "{}" because it\'s not stored'.format(tar))


