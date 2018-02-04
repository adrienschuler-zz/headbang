class Event:
    def __init__(self, storage):
        self.storage = storage
        self.index = 'headbang.facebook.events'
        self.type = 'event'

    def get(self, size: int = 10):
        '''
        '''
        events = self.storage.Elasticsearch.search(index=self.index, type=self.type,
            body={
            "size": size,
            "query": {
                "match_all": {}
            }
        })['hits']['hits']

        return list(map(lambda e: e['_source'], events))

    def post(self, events: dict):
        '''
        '''
        responses = []
        for event in events:
            response = self.storage.Elasticsearch.index(index=self.index, type=self.type,
                body=event, id=event['id'])
            responses.append(response)
        return responses
