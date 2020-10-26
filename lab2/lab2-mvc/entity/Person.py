class Person(object):
    def generator(self, list):
        if list is not None:
            return {'person_id': list[0],
                    'name': list[1],
                    'address': list[2],
                    'contact_email': list[3],
                    'contact_tel_num': list[4]}
        else:
            return {}