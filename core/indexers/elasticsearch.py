import json


def deep_get(dictionary: dict, keys: list) -> str:
    from functools import reduce
    return reduce(lambda d, key: d.get(key) if d else None, keys, dictionary)


class ESIndexer:
    def __init__(self, ESInstance):
        self.es = ESInstance

    def index(self, doc: dict) -> dict:
        return self.es.client.index(
            index=self.index,
            doc_type=self.type,
            body=doc)

    def bulk(self, docs: list) -> dict:
        bulk = self.format_bulk(docs)
        return self.es.client.bulk(
            index=self.index,
            doc_type=self.type,
            body=bulk)

    def format_bulk(self, docs: list, action: str = 'index') -> str:
        bulk = []
        for doc in docs:
            bulk.append({
                action: {
                    '_index': self.index,
                    '_type': self.type,
                    '_id': deep_get(doc, self.id_field)
                }
            })
            bulk.append(doc)
        return '\n'.join(json.dumps(entry) for entry in bulk)


class FoursquareVenue(ESIndexer):
    def __init__(self, ESInstance):
        super().__init__(ESInstance)
        self.index = 'foursquare.venues'
        self.type = 'venue'
        self.id_field = ['id']


class FacebookEvent(ESIndexer):
    def __init__(self, ESInstance):
        super().__init__(ESInstance)
        self.index = 'facebook.events'
        self.type = 'event'
        self.id_field = ['id']
