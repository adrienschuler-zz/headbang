from elasticsearch import Elasticsearch


class ES:
    def __init__(self, config):
        self.client = Elasticsearch(host=config['host'], port=config['port'])
