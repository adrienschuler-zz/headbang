from app import storage

print(storage)

ES = storage['es']

class Place(ES):
    def __init__(self):
        self.index = 'foursquare.venues'
        self.type = 'venue'
        self.id_field = 'id'

    def show():
        return {'foo': 'bar'}
