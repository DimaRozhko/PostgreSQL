class Thing(object):
    def generator(self, list):
        if list is not None:
            return {'thing_id': list[0],
                    'quantity': list[1],
                    'expiration_date': list[2],
                    'breakable': list[3],
                    'type_id': list[4],
                    'order_id': list[5],
                    'name': list[6]}
        else:
            return {}