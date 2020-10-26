class Departament(object):
    def generator(self, list):
        if list is not None:
            return {'departament_id': list[0],
                    'name': list[1],
                    'country': list[2]}
        else:
            return {}