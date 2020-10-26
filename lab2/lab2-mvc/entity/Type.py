class Type(object):
    def generator(self, list):
        if list is not None:
            return {'type_id': list[0],
                    'spoil_quick': list[1],
                    'type_name': list[2]}
        else:
            return {}