import json

from elasticsearch import Elasticsearch


class ES:
    def __init__(self, config):
        self.esclient = Elasticsearch(host=config['host'], port=config['port'])

    def index(self, doc: dict) -> dict:
        return self.esclient.index(
            index=self.index,
            doc_type=self.type,
            body=doc)

    def bulk(self, docs: list) -> dict:
        bulk = self.format_bulk(docs)
        return self.esclient.bulk(
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
                    '_id': doc[self.id_field]
                }
            })
            bulk.append(doc)
        return '\n'.join(json.dumps(entry) for entry in bulk)
