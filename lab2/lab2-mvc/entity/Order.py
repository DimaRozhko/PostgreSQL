class Order(object):
    def generator(self, list):
        if list is not None:
            return {'order_id': list[0],
                    'quantity': list[1],
                    'date': list[2],
                    'person_id': list[3]}
        else:
            return {}