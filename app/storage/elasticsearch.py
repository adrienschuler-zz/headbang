import json

from elasticsearch import Elasticsearch


class ES:
    def __init__(self, config):
        self.esclient = Elasticsearch(host=config['host'], port=config['port'])

    def index(self, index: str, type: str, doc: dict) -> dict:
        return self.esclient.index(
            index=index,
            doc_type=type,
            body=doc)

    def search(self, index: str, type: str, body: dict) -> dict:
        return self.esclient.search(
            index=index,
            doc_type=type,
            body=body)

    def bulk(self, index: str, type: str, docs: list) -> dict:
        bulk = self.format_bulk(docs)
        return self.esclient.bulk(
            index=index,
            doc_type=type,
            body=bulk)

    def format_bulk(self, index: str, type: str, docs: list, action: str = 'index') -> str:
        bulk = []
        for doc in docs:
            bulk.append({
                action: {
                    '_index': index,
                    '_type': type,
                    '_id': doc['id']
                }
            })
            bulk.append(doc)
        return '\n'.join(json.dumps(entry) for entry in bulk)
